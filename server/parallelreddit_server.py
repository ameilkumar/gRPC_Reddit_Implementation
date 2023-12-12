import logging
from concurrent import futures
import random
import sys

import sqlite3
from datetime import datetime

import grpc
import parallelreddit_pb2
import parallelreddit_pb2_grpc

NUMBER_OF_REPLY = 10


# Servicer for parallel reddit applications
class ParallelRedditServicer(parallelreddit_pb2_grpc.ParallelRedditServicer):
    # Create a post given post details
    # Return the created post
    def CreatePost(self, request, context):
        conn = sqlite3.connect('parallel_reddit.db')
        cursor = conn.cursor()
        # Add post to the Database

        # Convert enum to string
        if request.state == parallelreddit_pb2.PostState.HIDDEN_POST_STATE:
            state_string = "HIDDEN_POST_STATE"
        elif request.state == parallelreddit_pb2.PostState.NORMAL_POST_STATE:
            state_string = "NORMAL_POST_STATE"
        else:
            state_string = "LOCKED_POST_STATE"

        # Determine timestamp: 
        date = datetime.now().strftime('%Y-%m-%d')

        if request.image_url:
            # Insert data into the 'posts' table
            cursor.execute('''
                INSERT INTO posts (title, text, author, score, publication_date, subreddit_id, state, image_url)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                request.title,
                request.text,
                request.author.user_id,
                0,
                date,
                request.subreddit_id,
                state_string,
                request.image_url
            ))
        else:
            # Insert data into the 'posts' table
            cursor.execute('''
                INSERT INTO posts (title, text, author, score, publication_date, subreddit_id, state, video_url)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                request.title,
                request.text,
                request.author.user_id,
                0,
                date,
                request.subreddit_id,
                state_string,
                request.video_url
            ))
        # Save last row ID
        created_post_id = cursor.lastrowid
        conn.commit()
        # Close DB connection
        cursor.close()
        conn.close()

        # Make return object:
        response = parallelreddit_pb2.CreatePostResponse(
        post_created = parallelreddit_pb2.Post(
            title=request.title, 
            text=request.text, 
            author=request.author, 
            score=0, 
            publication_date=date, 
            subreddit_id=request.subreddit_id, 
            state=request.state, 
            post_id=created_post_id
            )
        )
        if request.image_url:
            response.post_created.image_url = request.image_url
        else:
            response.post_created.video_url = request.video_url
        # return the response
        return response
    
    # Upvotes a post given a post_id
    # Return the new score of the post
    def UpvotePost(self, request, context):
        # Get the score of the post from the DB
        conn = sqlite3.connect('parallel_reddit.db')
        cursor = conn.cursor()

        # Fetch the current score for the given post_id
        cursor.execute('SELECT score FROM posts WHERE post_id = ?', (request.post_id,))
        score = cursor.fetchone()[0]

        # Add 1 to the score
        score = score + 1
        # Modify the score in the DB
        cursor.execute('UPDATE posts SET score = ? WHERE post_id = ?', (score, request.post_id))
        conn.commit()

        # Close the connection
        cursor.close()
        conn.close()

        # Create response object with the new score
        return parallelreddit_pb2.UpvotePostResponse(newScore=score)

    # Downvotes a post given a post_id
    # Return the new score of the post
    def DownvotePost(self, request, context):
        # Get the score of the post from the DB
        conn = sqlite3.connect('parallel_reddit.db')
        cursor = conn.cursor()

        # Fetch the current score for the given post_id
        cursor.execute('SELECT score FROM posts WHERE post_id = ?', (request.post_id,))
        score = cursor.fetchone()[0]

        # Subtract 1 to the score
        score = score - 1
        # Modify the score in the DB
        cursor.execute('UPDATE posts SET score = ? WHERE post_id = ?', (score, request.post_id))
        conn.commit()

        # Close the connection
        cursor.close()
        conn.close()

        # Create response object with the new score
        return parallelreddit_pb2.DownvotePostResponse(newScore=score)
    
    # Retrieve and return all relevant post content given a post ID
    def RetrievePostContent(self, request, context):
        # Connect to DB
        conn = sqlite3.connect('parallel_reddit.db')
        cursor = conn.cursor()

        # Fetch the entire post based on post_id
        cursor.execute('SELECT * FROM posts WHERE post_id = ?', (request.post_id,))
        row = cursor.fetchone()

        # Close the connection
        cursor.close()
        conn.close()

        # Convert to dictionary
        post_columns = ['post_id', 'title', 'text', 'author', 'score', 'publication_date', 'subreddit_id', 'state', 'image_url', 'video_url']
        post_data = dict(zip(post_columns, row))
        # Define output object
        response = parallelreddit_pb2.RetrievePostResponse(
            title= post_data["title"], 
            text= post_data["text"], 
            author=parallelreddit_pb2.User(user_id=post_data["author"]), 
            score=post_data["score"],
            publication_date=post_data["publication_date"], 
            subreddit_id=post_data["subreddit_id"]
        )
        if post_data["state"] == "NORMAL_POST_STATE":
            response.state = parallelreddit_pb2.PostState.NORMAL_POST_STATE
        elif post_data["state"] == "LOCKED_POST_STATE":
            response.state = parallelreddit_pb2.PostState.LOCKED_POST_STATE
        else:
            response.state = parallelreddit_pb2.PostState.HIDDEN_POST_STATE
        
        if post_data.get("video_url"):
            response.video_url = post_data["video_url"]
        else:
            response.image_url = post_data["image_url"]

        # Return the response object
        return response
    
    def CreateComment(self, request, context):
        return super().CreateComment(request, context)
    
    # Create a comment given comment details
    # If it has a parent comment, adds to the parent comment's number of subcomments
    # Return the created comment
    def CreateComment(self, request, context):
        conn = sqlite3.connect('parallel_reddit.db')
        cursor = conn.cursor()
        # Add comment to the Database

        # Convert enum to string
        if request.state == parallelreddit_pb2.CommentState.HIDDEN_COMMENT_STATE:
            state_string = "HIDDEN_COMMENT_STATE"
        elif request.state == parallelreddit_pb2.CommentState.NORMAL_COMMENT_STATE:
            state_string = "NORMAL_COMMENT_STATE"

        # Determine timestamp: 
        date = datetime.now().strftime('%Y-%m-%d')

        if request.parent_comment_id:
            # Insert data into the 'comments' table
            cursor.execute('''
                INSERT INTO comments (author, content, score, publication_date, state, parent_comment_id, amountOfSubComments)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                request.author.user_id,
                request.content,
                0,
                date,
                state_string,
                request.parent_comment_id,
                0,
            ))

            # Add to the parent's amountOfSubComments
            cursor.execute('''
                UPDATE comments
                SET amountOfSubComments = amountOfSubComments + 1
                WHERE comment_id = ?
                ''', (request.parent_comment_id,)
    )
        else:
            # Insert data into the 'comments' table
            cursor.execute('''
                INSERT INTO comments (author, content, score, publication_date, state, parent_post_id, amountOfSubComments)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                request.author.user_id,
                request.content,
                0,
                date,
                state_string,
                request.parent_post_id,
                0,
            ))
        # Save last row ID
        created_comment_id = cursor.lastrowid
        conn.commit()
        # Close DB connection
        cursor.close()
        conn.close()

        # Make return object:
        response = parallelreddit_pb2.CreateCommentResponse(
        createdComment= parallelreddit_pb2.Comment(
            author=request.author, 
            score=0, 
            state=request.state, 
            publication_date=date, 
            comment_id=created_comment_id, 
            content=request.content, 
            amountOfSubComments=0
            )
        )
        if request.parent_post_id:
            response.createdComment.parent_post_id = request.parent_post_id
        else:
            response.createdComment.parent_comment_id = request.parent_comment_id
        # return the response
        return response
    
    # Upvotes a comment given a comment_id
    # Return the new score of the comment
    def UpvoteComment(self, request, context):
        # Get the score of the comment from the DB
        conn = sqlite3.connect('parallel_reddit.db')
        cursor = conn.cursor()

        # Fetch the current score for the given comment_id
        cursor.execute('SELECT score FROM comments WHERE comment_id = ?', (request.comment_id,))
        score = cursor.fetchone()[0]

        # Add 1 to the score
        score = score + 1
        # Modify the score in the DB
        cursor.execute('UPDATE comments SET score = ? WHERE comment_id = ?', (score, request.comment_id))
        conn.commit()

        # Close the connection
        cursor.close()
        conn.close()

        # Create response object with the new score
        return parallelreddit_pb2.UpvoteCommentResponse(newScore=score)
    
    # Downvotes a post given a comment_id
    # Return the new score of the comment
    def DownvoteComment(self, request, context):
        # Get the score of the comment from the DB
        conn = sqlite3.connect('parallel_reddit.db')
        cursor = conn.cursor()

        # Fetch the current score for the given comment_id
        cursor.execute('SELECT score FROM comments WHERE comment_id = ?', (request.comment_id,))
        score = cursor.fetchone()[0]

        # Subtract 1 to the score
        score = score - 1
        # Modify the score in the DB
        cursor.execute('UPDATE comments SET score = ? WHERE comment_id = ?', (score, request.comment_id))
        conn.commit()

        # Close the connection
        cursor.close()
        conn.close()

        # Create response object with the new score
        return parallelreddit_pb2.DownvoteCommentResponse(newScore=score)
    
    # Gets the N most upvoted comments under a post given a post ID and returns a list of the comments
    def MostUpvotedComments(self, request, context):
        conn = sqlite3.connect('parallel_reddit.db')
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM comments
            WHERE parent_post_id = ?
            ORDER BY score DESC
            LIMIT ?
        ''', (request.post_id, request.numberOfComments))

        comments_with_highest_score = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        conn.close()

        # Make output object
        total_comments = []
        for comment in comments_with_highest_score:
            user = parallelreddit_pb2.User(user_id=comment[1])
            collected_comment = parallelreddit_pb2.Comment( 
            score= comment[3],  
            publication_date=comment[4], 
            comment_id=comment[0], 
            content=comment[2], 
            amountOfSubComments=comment[8]
            )
            collected_comment.author.CopyFrom(user)
            #Handle state
            if comment[5] == "HIDDEN_COMMENT_STATE":
                collected_comment.state = parallelreddit_pb2.CommentState.HIDDEN_COMMENT_STATE
            else:
                collected_comment.state = parallelreddit_pb2.CommentState.NORMAL_COMMENT_STATE
            if comment[6] is not None:
                collected_comment.parent_post_id = comment[6]
            else:
                collected_comment.parent_comment_id = comment[7]
            total_comments.append(collected_comment)
            
        response = parallelreddit_pb2.MostUpvotedCommentsResponse(comments=total_comments)
        return response
        
    # given a root comment id and a number of comments, 
    # Return all comments belonging to a tree of the root comment, it's most upvoted comments, and their upvoted comments
    # Intentionally returned as a list with parent_comment_ids so tree can be extrapolated in any way desired from that
    def ExpandCommentBranch(self, request, context):
        
        conn = sqlite3.connect('parallel_reddit.db')
        cursor = conn.cursor()

        # Get root comment
        cursor.execute('''
        SELECT * FROM comments
        WHERE comment_id = ?
        ''', (request.commentId,))

        comment = cursor.fetchone()  # Retrieve the single comment

        user = parallelreddit_pb2.User(user_id=comment[1])
        root_comment = parallelreddit_pb2.Comment( 
            score=comment[3],  
            publication_date=comment[4], 
            comment_id=comment[0], 
            content=comment[2], 
            amountOfSubComments=comment[8]
        )
        root_comment.author.CopyFrom(user)
        # Handle state
        if comment[5] == "HIDDEN_COMMENT_STATE":
            root_comment.state = parallelreddit_pb2.CommentState.HIDDEN_COMMENT_STATE
        else:
            root_comment.state = parallelreddit_pb2.CommentState.NORMAL_COMMENT_STATE
        if comment[6] is not None:
            root_comment.parent_post_id = comment[6]
        else:
            root_comment.parent_comment_id = comment[7]

         # Get first level of tree
        cursor.execute('''
        SELECT * FROM comments
        WHERE parent_comment_id = ?
        ORDER BY score DESC
        LIMIT ?
        ''', (request.commentId, request.numberOfComments))

        comments_with_highest_score = cursor.fetchall()


        # comments
        first_level_comments = []
        for comment in comments_with_highest_score:
            user = parallelreddit_pb2.User(user_id=comment[1])
            collected_comment = parallelreddit_pb2.Comment( 
            score= comment[3],  
            publication_date=comment[4], 
            comment_id=comment[0], 
            content=comment[2], 
            amountOfSubComments=comment[8]
            )
            collected_comment.author.CopyFrom(user)
            #Handle state
            if comment[5] == "HIDDEN_COMMENT_STATE":
                collected_comment.state = parallelreddit_pb2.CommentState.HIDDEN_COMMENT_STATE
            else:
                collected_comment.state = parallelreddit_pb2.CommentState.NORMAL_COMMENT_STATE
            if comment[6] is not None:
                collected_comment.parent_post_id = comment[6]
            else:
                collected_comment.parent_comment_id = comment[7]
            first_level_comments.append(collected_comment)

        # Get second level of tree
        second_level_comments = []
        for comment in first_level_comments:
            cursor.execute('''
            SELECT * FROM comments
            WHERE parent_comment_id = ?
            ORDER BY score DESC
            LIMIT ?
            ''', (comment.comment_id, request.numberOfComments))

            comments_with_highest_score = cursor.fetchall()

            # comments
            for comment in comments_with_highest_score:
                user = parallelreddit_pb2.User(user_id=comment[1])
                collected_comment = parallelreddit_pb2.Comment( 
                score= comment[3],  
                publication_date=comment[4], 
                comment_id=comment[0], 
                content=comment[2], 
                amountOfSubComments=comment[8]
                )
                collected_comment.author.CopyFrom(user)
                #Handle state
                if comment[5] == "HIDDEN_COMMENT_STATE":
                    collected_comment.state = parallelreddit_pb2.CommentState.HIDDEN_COMMENT_STATE
                else:
                    collected_comment.state = parallelreddit_pb2.CommentState.NORMAL_COMMENT_STATE
                if comment[6] is not None:
                    collected_comment.parent_post_id = comment[6]
                else:
                    collected_comment.parent_comment_id = comment[7]
                second_level_comments.append(collected_comment)


        # Append all to list
        comment_tree_comments = [root_comment] + first_level_comments + second_level_comments
        # Add to return object
        comment_tree_response = parallelreddit_pb2.ExpandCommentBranchResponse(expandedComments=comment_tree_comments)

        # Close the cursor and database connection
        cursor.close()
        conn.close()
        return comment_tree_response
    
    #EXTRA CREDIT
    # Takes a stream of content, starting with a post and repeating with comments
    # Returns a stream of data providing updates on the state of all the monitored scores
    def MonitorUpdates(self, request_iterator, context):
        #Define post_id
        postId = -1
        # Define comment id list
        comments = []
        # for each request
        count = 0
        for request in request_iterator:
            if count == 0:
                postId = request.originalPostID
                count = count + 1
            elif request.addedCommentID is not None:
                comments.append(request.addedCommentID)
            
            #Obtain scores:
            conn = sqlite3.connect('parallel_reddit.db')
            cursor = conn.cursor()

            # Fetch the current score for the given post_id
            cursor.execute('SELECT score FROM posts WHERE post_id = ?', (postId,))
            newPostScore = cursor.fetchone()[0]
            # for each comment, obtain the score and map it
            comment_scores = {}
            for commentID in comments:
                cursor.execute('SELECT score FROM comments WHERE comment_id = ?', (commentID,))
                comment_scores[commentID] = cursor.fetchone()[0]
            # Close DB connection
            cursor.close()
            conn.close()

            # Create response object
            response = parallelreddit_pb2.MonitorUpdatesResponse(postID=postId, postScore=newPostScore, commentScores=comment_scores)
            yield response
            


# Start the server. Sets [::]:50051 as default host/port
def serve(host = "[::]", port = "50051"):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    parallelreddit_pb2_grpc.add_ParallelRedditServicer_to_server(ParallelRedditServicer(), server)

    server.add_insecure_port(host + ":" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

# EXTRA CREDIT
# Set up the database using SQlite
def set_up_db():
    # Define connection to the Database
    conn = sqlite3.connect('parallel_reddit.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            post_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            text TEXT,
            author TEXT,
            score INTEGER,
            publication_date TEXT,
            subreddit_id TEXT,
            state TEXT,
            image_url TEXT,
            video_url TEXT
        )
    ''')
    conn.commit()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            author TEXT,
            content TEXT,
            score INTEGER,
            publication_date TEXT,
            state TEXT,
            parent_post_id INTEGER,
            parent_comment_id INTEGER, 
            amountOfSubComments INTEGER
        )
    ''')
    conn.commit()
    # Close DB connection
    cursor.close()
    conn.close()


if __name__ == "__main__":
    # Default host
    host = "[::]"
    # Default port
    port = "50051"
    # Check for command line arguments
    arguments = sys.argv[1:]
    if len(arguments) > 1:
        host = arguments[0]
    if len(arguments) > 2:
        port = arguments[1]
    logging.basicConfig()

    # Set up database with SQLite
    set_up_db()
    # call serve with host, and port
    serve(host, port)

