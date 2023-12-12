import parallelreddit_client
import unittest
from unittest.mock import MagicMock

# Tested 4 high level functions with Mock per Piazza post @176
# 4 high level function implementations

# High level function to retrieve a post given a post_id
def retrieve_post(client, post_id):
     result = client.retrieve_post_content(post_id)
     return result

# Retrieve the most upvoted comments under the post
def retrieve_n_most_upvoted_comments(client, post_id, n):
     # Retrieve the n most upvoted comments under post_id
     result = client.get_most_upvoted_comments(post_id, n)
     return result

# Expand the most upvoted comment under a post n times
def expand_most_upvoted_comment(client, post_id, n):
     # Get the most upvoted comment under the post
     comment_id = client.get_most_upvoted_comments(post_id, 1)
     # Expand the comment branch n X n
     result = client.expand_comment_branch(comment_id[0], n)
     return result

     # Return the most upvoted reply under the most upvoted comment,
     # or None if there are no comments or no replies under the most upvoted one
     # The wording was not clear here so I am stating my assumption: reply means directly under the top comment(the first layer in the tree)
def most_upvoted_reply_under_most_upvoted_comment(client, post_id):
     # Get the most upvoted comment under the post
     comment_id = client.get_most_upvoted_comments(post_id, 1)
     # expand to get most upvoted reply X 1
     expanded = client.expand_comment_branch(comment_id, 1)
     # Will be at most, tree of height 2 with the top reply being at level 1 in the tree
     result = expanded[1]
     # Will be None if there are no commentr or replies under the most upvoted one
     return result
    



# Test class for parallel reddit
# Tested 4 high level functions with Mock per Piazza post @176
# Unit testing of client code was not forgotten and was done using postman and manually(see client if __name__ == '__main__ for some reference)
class TestParallelReddit(unittest.TestCase):

    # Test retrieve post business logic
     def test_retrieve_post(self):
            # Create a mock client
            mock_client = MagicMock()

            # Call the function with post_id 1
            post_id = 1
            retrieve_post(mock_client, post_id)

            # Assert that the retrieve_post_content method was called with the correct argument
            mock_client.retrieve_post_content.assert_called_once_with(post_id)

    # Test retrieve n most upvoted comments business logic
     def test_retrieve_n_most_upvoted_comments(self):
        # Create a mock client
        mock_client = MagicMock()
        # Call with post ID 1 and n = 5
        post_id = 1
        n = 5 
        retrieve_n_most_upvoted_comments(mock_client, post_id, n)

        # Assert that the get_most_upvoted_comments was called once with the correct arguments
        mock_client.get_most_upvoted_comments.assert_called_once_with(post_id, n)

    # Test expand the most upvoted comment business logic
     def test_expand_most_upvoted_comment(self):
        # Create a mock client
        mock_client = MagicMock()
        # Call with post Id 1 and n = 5
        post_id = 1
        n = 5
        # Mock the most upvoted comments return value to be [1]
        mock_client.get_most_upvoted_comments.return_value = [1]

        expand_most_upvoted_comment(mock_client, post_id, n)

        # Assert that client.expand_comment_branch was called once with the correct arguments
        mock_client.expand_comment_branch.assert_called_once_with(1, n)

     # Test getting the most upvoted reply under the most upvoted comment business logic
     def test_most_upvoted_reply_under_most_upvoted_comment(self):
        # Create mock client
        mock_client = MagicMock()

        # Mock the expected comment_Id to be 3
        mock_client.get_most_upvoted_comments.return_value = 3


        # Call with post ID = 1
        post_id = 1
        most_upvoted_reply_under_most_upvoted_comment(mock_client, post_id)


        # Assert that get_most_upvoted_comments and expand_comment_branch were only called once
        mock_client.get_most_upvoted_comments.assert_called_once_with(post_id, 1)
        mock_client.expand_comment_branch.assert_called_once_with(3, 1)


if __name__ == '__main__':
    unittest.main()