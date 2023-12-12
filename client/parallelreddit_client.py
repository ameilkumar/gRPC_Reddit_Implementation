from __future__ import print_function

import logging

import grpc
# Import generated files
import parallelreddit_pb2
import parallelreddit_pb2_grpc

# Represent the Enums to hide the implementation
class PostState:
    NORMAL_POST_STATE = 0
    LOCKED_POST_STATE = 1
    HIDDEN_POST_STATE = 2
   
class CommentState:
    NORMAL_COMMENT_STATE = 0
    HIDDEN_COMMENT_STATE = 1

class SubredditState:
    PUBLIC_SUBREDDIT_STATE = 0
    PRIVATE_SUBREDDIT_STATE = 1
    HIDDEN_SUBREDDIT_STATE = 2

# Client definition
class ParallelRedditClient:
    # Constructor that takes host and port as initialization variables
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.channel = grpc.insecure_channel(f"{self.host}:{self.port}")
        self.stub = parallelreddit_pb2_grpc.ParallelRedditStub(self.channel)

    # Takes post details as a dictionary and returns a dictionary containing the created post
    def create_post(self, post_details):
        # Convert Post dictionary into CreatePostRequest object
        create_post_request = parallelreddit_pb2.CreatePostRequest()
        user = parallelreddit_pb2.User(user_id=post_details["author"])
        if post_details.get("title"):
            create_post_request.title = post_details["title"]
        if post_details.get("text"):
            create_post_request.text = post_details["text"]
        if post_details.get("image_url"):
            create_post_request.image_url = post_details["image_url"]
        elif post_details.get("video_url"):
            create_post_request.video_url = post_details["video_url"]
        if post_details.get("author"):
            create_post_request.author.CopyFrom(user)
        if post_details.get("state"):
            state = post_details["state"]
            if state == PostState.NORMAL_POST_STATE:
                create_post_request.state = parallelreddit_pb2.PostState.NORMAL_POST_STATE
            elif state == PostState.LOCKED_POST_STATE:
                create_post_request.state = parallelreddit_pb2.PostState.LOCKED_POST_STATE
            elif state == PostState.HIDDEN_POST_STATE:
                create_post_request.state = parallelreddit_pb2.PostState.HIDDEN_POST_STATE
        if post_details.get("subreddit_id"):
            create_post_request.subreddit_id = post_details["subreddit_id"]
        
        # Call server with object
        response = self.stub.CreatePost(create_post_request)

        # Convert response into created post dictionary to return
        response_dict = {
            "title": response.post_created.title, 
            "text": response.post_created.text, 
            "author": response.post_created.author.user_id, 
            "score": response.post_created.score,
            "publication_date": response.post_created.publication_date,
            "post_id": response.post_created.post_id,
            "subreddit_id": response.post_created.subreddit_id
            }
        if response.post_created.state == parallelreddit_pb2.PostState.NORMAL_POST_STATE:
            response_dict["state"] = PostState.NORMAL_POST_STATE
        elif response.post_created.state == parallelreddit_pb2.PostState.LOCKED_POST_STATE:
            response_dict["state"] = PostState.LOCKED_POST_STATE
        elif response.post_created.state == parallelreddit_pb2.PostState.HIDDEN_POST_STATE:
            response_dict["state"] = PostState.HIDDEN_POST_STATE
        if response.post_created.video_url:
            response_dict["video_url"] = response.post_created.video_url
        elif response.post_created.image_url:
            response_dict["image_url"] = response.post_created.image_url

        # Return the created dictionary
        return response_dict
    
    # Upvotes a post given a post ID
    # returns the new post score
    def upvote_post(self, input_post_id):
        # Create request object
        upvote_post_request = parallelreddit_pb2.UpvotePostRequest(post_id=input_post_id)
        # Call server with object
        response = self.stub.UpvotePost(upvote_post_request)

        # Return the new score
        return response.newScore
    
    # Downvotes a post given a post ID
    # returns the new post score
    def downvote_post(self, input_post_id):
        # Create request object
        downvote_post_request = parallelreddit_pb2.DownvotePostRequest(post_id=input_post_id)
        # Call server with object
        response = self.stub.DownvotePost(downvote_post_request)

        # Return the new score
        return response.newScore

    # Retrieves the content of a post from given input post id
    # Returns all relevant information about the post as a dictionary
    def retrieve_post_content(self, input_post_id):
        # Define the request object
        retrieve_post_content_request = parallelreddit_pb2.RetrievePostRequest(post_id=input_post_id)
        # call server with object
        response = self.stub.RetrievePostContent(retrieve_post_content_request)

        # Convert response into created post dictionary to return
        response_dict = {
            "title": response.title, 
            "text": response.text, 
            "author": response.author.user_id, 
            "score": response.score,
            "publication_date": response.publication_date,
            "subreddit_id": response.subreddit_id
            }
        if response.state == parallelreddit_pb2.PostState.NORMAL_POST_STATE:
            response_dict["state"] = PostState.NORMAL_POST_STATE
        elif response.state == parallelreddit_pb2.PostState.LOCKED_POST_STATE:
            response_dict["state"] = PostState.LOCKED_POST_STATE
        elif response.state == parallelreddit_pb2.PostState.HIDDEN_POST_STATE:
            response_dict["state"] = PostState.HIDDEN_POST_STATE
        if response.video_url:
            response_dict["video_url"] = response.video_url
        elif response.image_url:
            response_dict["image_url"] = response.image_url

        # Return dictionary
        return response_dict
    
    # Takes comment details as a dictionary and returns a dictionary containing the created comment
    def create_comment(self, comment_details):
        # Convert Comment dictionary into CreateCommentRequest object
        create_comment_request = parallelreddit_pb2.CreateCommentRequest()
        user = parallelreddit_pb2.User(user_id=comment_details["author"])
        if comment_details.get("content"):
            create_comment_request.content = comment_details["content"]
        if comment_details.get("parent_post_id"):
            create_comment_request.parent_post_id = comment_details["parent_post_id"]
        elif comment_details.get("parent_comment_id"):
            create_comment_request.parent_comment_id = comment_details["parent_comment_id"]
        if comment_details.get("author"):
            create_comment_request.author.CopyFrom(user)
        if comment_details.get("state"):
            state = comment_details["state"]
            if state == CommentState.NORMAL_COMMENT_STATE:
                create_comment_request.state = parallelreddit_pb2.CommentState.NORMAL_COMMENT_STATE
            elif state == CommentState.HIDDEN_COMMENT_STATE:
                create_comment_request.state = parallelreddit_pb2.CommentState.HIDDEN_COMMENT_STATE
        
        # Call server with object
        response = self.stub.CreateComment(create_comment_request)

        # Convert response into created comment dictionary to return
        response_dict = {
            "content": response.createdComment.content, 
            "author": response.createdComment.author.user_id, 
            "score": response.createdComment.score,
            "publication_date": response.createdComment.publication_date,
            "comment_id": response.createdComment.comment_id,
            "amountOfSubComments": response.createdComment.amountOfSubComments
            }
        if response.createdComment.state == parallelreddit_pb2.CommentState.NORMAL_COMMENT_STATE:
            response_dict["state"] = CommentState.NORMAL_COMMENT_STATE
        elif response.createdComment.state == parallelreddit_pb2.CommentState.HIDDEN_COMMENT_STATE:
            response_dict["state"] = CommentState.HIDDEN_COMMENT_STATE
        if response.createdComment.parent_post_id:
            response_dict["parent_post_id"] = response.createdComment.parent_post_id
        elif response.createdComment.parent_comment_id:
            response_dict["parent_comment_id"] = response.createdComment.parent_comment_id

        # Return the created dictionary
        return response_dict
    
    # Upvotes a comment given a comment ID
    # returns the new comment score
    def upvote_comment(self, input_comment_id):
        # Create request object
        upvote_comment_request = parallelreddit_pb2.UpvoteCommentRequest(comment_id=input_comment_id)
        # Call server with object
        response = self.stub.UpvoteComment(upvote_comment_request)

        # Return the new score
        return response.newScore
    
    # Downvotes a comment given a comment ID
    # returns the new comment score
    def downvote_comment(self, input_comment_id):
        # Create request object
        downvote_comment_request = parallelreddit_pb2.DownvoteCommentRequest(comment_id=input_comment_id)
        # Call server with object
        response = self.stub.DownvoteComment(downvote_comment_request)

        # Return the new score
        return response.newScore

    # Returns an array containing comments(represented in a dictionary) corresponding to the n most upvoted comments under a given post_id
    # It will only be comments directy under the post, but information on the amount of subcomments it has will be presented for each comment returned
    def get_most_upvoted_comments(self, input_post_id, number_of_comments):
        # Create request object 
        get_most_upvoted_request = parallelreddit_pb2.MostUpvotedCommentsRequest(post_id=input_post_id, numberOfComments=number_of_comments)
        # Call the server with the object
        response = self.stub.MostUpvotedComments(get_most_upvoted_request)
        # Create return array from returned data
        comment_array = []
        for comment in response.comments:
            comment_dict = {}
            comment_dict["author"] = comment.author.user_id
            comment_dict["score"] = comment.score
            comment_dict["publication_date"] = comment.publication_date
            comment_dict["comment_id"] = comment.comment_id
            comment_dict["content"] = comment.content
            comment_dict["amountOfSubComments"] = comment.amountOfSubComments
            if comment.parent_post_id: 
                comment_dict["parent_post_id"] = comment.parent_post_id
            elif comment.parent_comment_id:
                comment_dict["parent_comment_id"] = comment.parent_comment_id
            if comment.state == CommentState.HIDDEN_COMMENT_STATE:
                comment_dict["comment_state"] = "HIDDEN_COMMENT_STATE"
            elif comment.state == CommentState.NORMAL_COMMENT_STATE:
                comment_dict["comment_state"] = "NORMAL_COMMENT_STATE"
            comment_array.append(comment_dict)

        return comment_array
    
    # Returns an array containing comments(represented in a dictionary) corresponding to comments in a tree containing:
    # The root comment provided, the n most upvoted subcomments, and the n most upvoted subcomments of those comments given n as input number of comments
    # Each comment in the list contains a commentID and parent commentID so it can effectively be interpreted as a tree. 
    def expand_comment_branch(self, input_comment_id, number_of_comments):
        # Define input
        expand_comment_branch_request = parallelreddit_pb2.ExpandCommentBranchRequest(commentId=input_comment_id, numberOfComments=number_of_comments)
        # Call server with the object
        response = self.stub.ExpandCommentBranch(expand_comment_branch_request)

        # Create return array from returned data
        comment_array = []
        for comment in response.expandedComments:
            comment_dict = {}
            comment_dict["author"] = comment.author.user_id
            comment_dict["score"] = comment.score
            comment_dict["publication_date"] = comment.publication_date
            comment_dict["comment_id"] = comment.comment_id
            comment_dict["content"] = comment.content
            comment_dict["amountOfSubComments"] = comment.amountOfSubComments
            if comment.parent_post_id: 
                comment_dict["parent_post_id"] = comment.parent_post_id
            elif comment.parent_comment_id:
                comment_dict["parent_comment_id"] = comment.parent_comment_id
            if comment.state == CommentState.HIDDEN_COMMENT_STATE:
                comment_dict["comment_state"] = "HIDDEN_COMMENT_STATE"
            elif comment.state == CommentState.NORMAL_COMMENT_STATE:
                comment_dict["comment_state"] = "NORMAL_COMMENT_STATE"
            comment_array.append(comment_dict)

        return comment_array
    
    # Takes in an iterator that first gives a post ID, followed by any number of commentID's. Returns a stream of the scores corresponding
    # To the post and each comment for each additional comment measured in dictionary format
    def monitor_updates(self, content_iterator):
        # Convert content in iterator to appropriate objects
        monitor_objects_iterator = self._convert_to_monitor_object_iterator(content_iterator)
        # Call server with the iterator
        response_iterator = self.stub.MonitorUpdates(monitor_objects_iterator)
        for response in response_iterator:
            # Convert to dict object corresponding to score data
            clean_response = {}
            clean_response["postID"] = response.postID
            clean_response["postScore"] = response.postScore
            clean_response["commentScores"] = response.commentScores
            yield clean_response

    # Helper function to convert post/comment id iteration to MonitorUpdatesRequest objects for monitor_updates()
    # Assumes first item is the post, followed by comments
    def _convert_to_monitor_object_iterator(self, content_iterator):
        count = 0
        for content in content_iterator:
            if count == 0:
                count = count + 1
                yield parallelreddit_pb2.MonitorUpdatesRequest(originalPostID=content)
            else:
                yield parallelreddit_pb2.MonitorUpdatesRequest(addedCommentID=content)


# Some basic tests. May need adjustment of values if running from scratch with empty server DB
# This is not part of assignment. Just some reference
if __name__ == "__main__":
    client = ParallelRedditClient("localhost", "50051")
    post_details = {
    "title": "Sample Title",
    "text": "Sample text content",
    "image_url": "https://example.com/image.jpg",
    "author": "user123",
    "state": PostState.NORMAL_POST_STATE,
    "subreddit_id": "terrariums"
    }
    result = client.create_post(post_details)
    print(result)
    post_details = {
    "title": "Sample Title",
    "text": "Sample text content",
    "video_url": "https://example.com/image.jpg",
    "author": "user123",
    "state": PostState.LOCKED_POST_STATE,
    "subreddit_id": "tools"
    }
    result = client.create_post(post_details)
    print(result)
    upvoted = client.upvote_post(result["post_id"])
    print(upvoted)
    upvoted = client.upvote_post(result["post_id"])
    print(upvoted)
    downvoted = client.downvote_post(result["post_id"])
    print(downvoted)
    downvoted = client.downvote_post(result["post_id"])
    print(downvoted)
    downvoted = client.downvote_post(result["post_id"])
    print(downvoted)
    get_content = client.retrieve_post_content(result["post_id"])
    print(get_content)

    comment_details = {
    "author": "user123",
    "parent_post_id": 3,
    "state": CommentState.NORMAL_COMMENT_STATE,
    "content": "Some stuff that represents a comment",  
    }
    create_comment_result = client.create_comment(comment_details)
    print(create_comment_result)

    comment_details_2 = {
    "author": "user123",
    "parent_post_id": 1,
    "state": CommentState.HIDDEN_COMMENT_STATE,
    "content": "Some stuff that represents a comment",  
    }
    create_comment_result_2 = client.create_comment(comment_details_2)
    upvoted = client.upvote_comment(create_comment_result_2["comment_id"])
    upvoted = client.upvote_comment(create_comment_result_2["comment_id"])
    upvoted = client.upvote_comment(create_comment_result_2["comment_id"])
    upvoted = client.upvote_comment(create_comment_result_2["comment_id"])
    upvoted = client.upvote_comment(create_comment_result_2["comment_id"])
    print(create_comment_result_2)
    comment_details_2 = {
    "author": "user123",
    "parent_comment_id": create_comment_result_2["comment_id"],
    "state": CommentState.HIDDEN_COMMENT_STATE,
    "content": "Some stuff that represents a comment",  
    }
    create_comment_result_2 = client.create_comment(comment_details_2)
    upvoted = client.upvote_comment(create_comment_result_2["comment_id"])
    upvoted = client.upvote_comment(create_comment_result_2["comment_id"])
    upvoted = client.upvote_comment(create_comment_result_2["comment_id"])
    upvoted = client.upvote_comment(create_comment_result_2["comment_id"])
    upvoted = client.upvote_comment(create_comment_result_2["comment_id"])
    print(upvoted)
    upvoted = client.upvote_comment(create_comment_result["comment_id"])
    print(upvoted)
    downvoted = client.downvote_comment(create_comment_result["comment_id"])
    print(downvoted)
    downvoted = client.downvote_comment(create_comment_result["comment_id"])
    print(downvoted)
    downvoted = client.downvote_comment(create_comment_result["comment_id"])
    print(downvoted)
    most_upvoted = client.get_most_upvoted_comments(1, 2)
    print("MOST UPVOTED"+str(most_upvoted))

    expand_results = client.expand_comment_branch(1, 4)
    print(expand_results)
    iterator = client.monitor_updates(iter([1, 2, 3, 4]))
    for content in iterator:
        print(content)
