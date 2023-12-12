# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import parallelreddit_pb2 as parallelreddit__pb2


class ParallelRedditStub(object):
    """The ParallelReddit service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreatePost = channel.unary_unary(
                '/parallelreddit.ParallelReddit/CreatePost',
                request_serializer=parallelreddit__pb2.CreatePostRequest.SerializeToString,
                response_deserializer=parallelreddit__pb2.CreatePostResponse.FromString,
                )
        self.UpvotePost = channel.unary_unary(
                '/parallelreddit.ParallelReddit/UpvotePost',
                request_serializer=parallelreddit__pb2.UpvotePostRequest.SerializeToString,
                response_deserializer=parallelreddit__pb2.UpvotePostResponse.FromString,
                )
        self.DownvotePost = channel.unary_unary(
                '/parallelreddit.ParallelReddit/DownvotePost',
                request_serializer=parallelreddit__pb2.DownvotePostRequest.SerializeToString,
                response_deserializer=parallelreddit__pb2.DownvotePostResponse.FromString,
                )
        self.RetrievePostContent = channel.unary_unary(
                '/parallelreddit.ParallelReddit/RetrievePostContent',
                request_serializer=parallelreddit__pb2.RetrievePostRequest.SerializeToString,
                response_deserializer=parallelreddit__pb2.RetrievePostResponse.FromString,
                )
        self.CreateComment = channel.unary_unary(
                '/parallelreddit.ParallelReddit/CreateComment',
                request_serializer=parallelreddit__pb2.CreateCommentRequest.SerializeToString,
                response_deserializer=parallelreddit__pb2.CreateCommentResponse.FromString,
                )
        self.UpvoteComment = channel.unary_unary(
                '/parallelreddit.ParallelReddit/UpvoteComment',
                request_serializer=parallelreddit__pb2.UpvoteCommentRequest.SerializeToString,
                response_deserializer=parallelreddit__pb2.UpvoteCommentResponse.FromString,
                )
        self.DownvoteComment = channel.unary_unary(
                '/parallelreddit.ParallelReddit/DownvoteComment',
                request_serializer=parallelreddit__pb2.DownvoteCommentRequest.SerializeToString,
                response_deserializer=parallelreddit__pb2.DownvoteCommentResponse.FromString,
                )
        self.MostUpvotedComments = channel.unary_unary(
                '/parallelreddit.ParallelReddit/MostUpvotedComments',
                request_serializer=parallelreddit__pb2.MostUpvotedCommentsRequest.SerializeToString,
                response_deserializer=parallelreddit__pb2.MostUpvotedCommentsResponse.FromString,
                )
        self.ExpandCommentBranch = channel.unary_unary(
                '/parallelreddit.ParallelReddit/ExpandCommentBranch',
                request_serializer=parallelreddit__pb2.ExpandCommentBranchRequest.SerializeToString,
                response_deserializer=parallelreddit__pb2.ExpandCommentBranchResponse.FromString,
                )
        self.MonitorUpdates = channel.stream_stream(
                '/parallelreddit.ParallelReddit/MonitorUpdates',
                request_serializer=parallelreddit__pb2.MonitorUpdatesRequest.SerializeToString,
                response_deserializer=parallelreddit__pb2.MonitorUpdatesResponse.FromString,
                )


class ParallelRedditServicer(object):
    """The ParallelReddit service definition.
    """

    def CreatePost(self, request, context):
        """Creates a post
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpvotePost(self, request, context):
        """Upvote a post
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownvotePost(self, request, context):
        """Downvote a post
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrievePostContent(self, request, context):
        """Retrieve post content
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateComment(self, request, context):
        """Create a comment
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpvoteComment(self, request, context):
        """Upvote a comment
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownvoteComment(self, request, context):
        """Downvote a comment
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MostUpvotedComments(self, request, context):
        """Retrieve list of N most upvoted comments under a post
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExpandCommentBranch(self, request, context):
        """Expand comment branch
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MonitorUpdates(self, request_iterator, context):
        """EXTRA CREDIT: Monitor updates
        Need a bidirectional stream
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ParallelRedditServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreatePost': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePost,
                    request_deserializer=parallelreddit__pb2.CreatePostRequest.FromString,
                    response_serializer=parallelreddit__pb2.CreatePostResponse.SerializeToString,
            ),
            'UpvotePost': grpc.unary_unary_rpc_method_handler(
                    servicer.UpvotePost,
                    request_deserializer=parallelreddit__pb2.UpvotePostRequest.FromString,
                    response_serializer=parallelreddit__pb2.UpvotePostResponse.SerializeToString,
            ),
            'DownvotePost': grpc.unary_unary_rpc_method_handler(
                    servicer.DownvotePost,
                    request_deserializer=parallelreddit__pb2.DownvotePostRequest.FromString,
                    response_serializer=parallelreddit__pb2.DownvotePostResponse.SerializeToString,
            ),
            'RetrievePostContent': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrievePostContent,
                    request_deserializer=parallelreddit__pb2.RetrievePostRequest.FromString,
                    response_serializer=parallelreddit__pb2.RetrievePostResponse.SerializeToString,
            ),
            'CreateComment': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateComment,
                    request_deserializer=parallelreddit__pb2.CreateCommentRequest.FromString,
                    response_serializer=parallelreddit__pb2.CreateCommentResponse.SerializeToString,
            ),
            'UpvoteComment': grpc.unary_unary_rpc_method_handler(
                    servicer.UpvoteComment,
                    request_deserializer=parallelreddit__pb2.UpvoteCommentRequest.FromString,
                    response_serializer=parallelreddit__pb2.UpvoteCommentResponse.SerializeToString,
            ),
            'DownvoteComment': grpc.unary_unary_rpc_method_handler(
                    servicer.DownvoteComment,
                    request_deserializer=parallelreddit__pb2.DownvoteCommentRequest.FromString,
                    response_serializer=parallelreddit__pb2.DownvoteCommentResponse.SerializeToString,
            ),
            'MostUpvotedComments': grpc.unary_unary_rpc_method_handler(
                    servicer.MostUpvotedComments,
                    request_deserializer=parallelreddit__pb2.MostUpvotedCommentsRequest.FromString,
                    response_serializer=parallelreddit__pb2.MostUpvotedCommentsResponse.SerializeToString,
            ),
            'ExpandCommentBranch': grpc.unary_unary_rpc_method_handler(
                    servicer.ExpandCommentBranch,
                    request_deserializer=parallelreddit__pb2.ExpandCommentBranchRequest.FromString,
                    response_serializer=parallelreddit__pb2.ExpandCommentBranchResponse.SerializeToString,
            ),
            'MonitorUpdates': grpc.stream_stream_rpc_method_handler(
                    servicer.MonitorUpdates,
                    request_deserializer=parallelreddit__pb2.MonitorUpdatesRequest.FromString,
                    response_serializer=parallelreddit__pb2.MonitorUpdatesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'parallelreddit.ParallelReddit', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ParallelReddit(object):
    """The ParallelReddit service definition.
    """

    @staticmethod
    def CreatePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/parallelreddit.ParallelReddit/CreatePost',
            parallelreddit__pb2.CreatePostRequest.SerializeToString,
            parallelreddit__pb2.CreatePostResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpvotePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/parallelreddit.ParallelReddit/UpvotePost',
            parallelreddit__pb2.UpvotePostRequest.SerializeToString,
            parallelreddit__pb2.UpvotePostResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DownvotePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/parallelreddit.ParallelReddit/DownvotePost',
            parallelreddit__pb2.DownvotePostRequest.SerializeToString,
            parallelreddit__pb2.DownvotePostResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetrievePostContent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/parallelreddit.ParallelReddit/RetrievePostContent',
            parallelreddit__pb2.RetrievePostRequest.SerializeToString,
            parallelreddit__pb2.RetrievePostResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/parallelreddit.ParallelReddit/CreateComment',
            parallelreddit__pb2.CreateCommentRequest.SerializeToString,
            parallelreddit__pb2.CreateCommentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpvoteComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/parallelreddit.ParallelReddit/UpvoteComment',
            parallelreddit__pb2.UpvoteCommentRequest.SerializeToString,
            parallelreddit__pb2.UpvoteCommentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DownvoteComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/parallelreddit.ParallelReddit/DownvoteComment',
            parallelreddit__pb2.DownvoteCommentRequest.SerializeToString,
            parallelreddit__pb2.DownvoteCommentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MostUpvotedComments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/parallelreddit.ParallelReddit/MostUpvotedComments',
            parallelreddit__pb2.MostUpvotedCommentsRequest.SerializeToString,
            parallelreddit__pb2.MostUpvotedCommentsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExpandCommentBranch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/parallelreddit.ParallelReddit/ExpandCommentBranch',
            parallelreddit__pb2.ExpandCommentBranchRequest.SerializeToString,
            parallelreddit__pb2.ExpandCommentBranchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MonitorUpdates(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/parallelreddit.ParallelReddit/MonitorUpdates',
            parallelreddit__pb2.MonitorUpdatesRequest.SerializeToString,
            parallelreddit__pb2.MonitorUpdatesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
