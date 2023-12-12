from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PostState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    NORMAL_POST_STATE: _ClassVar[PostState]
    LOCKED_POST_STATE: _ClassVar[PostState]
    HIDDEN_POST_STATE: _ClassVar[PostState]

class CommentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    NORMAL_COMMENT_STATE: _ClassVar[CommentState]
    HIDDEN_COMMENT_STATE: _ClassVar[CommentState]

class SubredditState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PUBLIC_SUBREDDIT_STATE: _ClassVar[SubredditState]
    PRIVATE_SUBREDDIT_STATE: _ClassVar[SubredditState]
    HIDDEN_SUBREDDIT_STATE: _ClassVar[SubredditState]
NORMAL_POST_STATE: PostState
LOCKED_POST_STATE: PostState
HIDDEN_POST_STATE: PostState
NORMAL_COMMENT_STATE: CommentState
HIDDEN_COMMENT_STATE: CommentState
PUBLIC_SUBREDDIT_STATE: SubredditState
PRIVATE_SUBREDDIT_STATE: SubredditState
HIDDEN_SUBREDDIT_STATE: SubredditState

class User(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class Post(_message.Message):
    __slots__ = ["title", "text", "image_url", "video_url", "author", "score", "state", "publication_date", "post_id", "subreddit_id"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    SUBREDDIT_ID_FIELD_NUMBER: _ClassVar[int]
    title: str
    text: str
    image_url: str
    video_url: str
    author: User
    score: int
    state: PostState
    publication_date: str
    post_id: int
    subreddit_id: str
    def __init__(self, title: _Optional[str] = ..., text: _Optional[str] = ..., image_url: _Optional[str] = ..., video_url: _Optional[str] = ..., author: _Optional[_Union[User, _Mapping]] = ..., score: _Optional[int] = ..., state: _Optional[_Union[PostState, str]] = ..., publication_date: _Optional[str] = ..., post_id: _Optional[int] = ..., subreddit_id: _Optional[str] = ...) -> None: ...

class Comment(_message.Message):
    __slots__ = ["author", "parent_post_id", "parent_comment_id", "score", "state", "publication_date", "comment_id", "content", "amountOfSubComments"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    PARENT_POST_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    AMOUNTOFSUBCOMMENTS_FIELD_NUMBER: _ClassVar[int]
    author: User
    parent_post_id: int
    parent_comment_id: int
    score: int
    state: CommentState
    publication_date: str
    comment_id: int
    content: str
    amountOfSubComments: int
    def __init__(self, author: _Optional[_Union[User, _Mapping]] = ..., parent_post_id: _Optional[int] = ..., parent_comment_id: _Optional[int] = ..., score: _Optional[int] = ..., state: _Optional[_Union[CommentState, str]] = ..., publication_date: _Optional[str] = ..., comment_id: _Optional[int] = ..., content: _Optional[str] = ..., amountOfSubComments: _Optional[int] = ...) -> None: ...

class Subreddit(_message.Message):
    __slots__ = ["name", "state", "tags", "subreddit_id"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    SUBREDDIT_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: SubredditState
    tags: _containers.RepeatedScalarFieldContainer[str]
    subreddit_id: str
    def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[SubredditState, str]] = ..., tags: _Optional[_Iterable[str]] = ..., subreddit_id: _Optional[str] = ...) -> None: ...

class CreatePostRequest(_message.Message):
    __slots__ = ["title", "text", "image_url", "video_url", "author", "score", "state", "subreddit_id"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SUBREDDIT_ID_FIELD_NUMBER: _ClassVar[int]
    title: str
    text: str
    image_url: str
    video_url: str
    author: User
    score: int
    state: PostState
    subreddit_id: str
    def __init__(self, title: _Optional[str] = ..., text: _Optional[str] = ..., image_url: _Optional[str] = ..., video_url: _Optional[str] = ..., author: _Optional[_Union[User, _Mapping]] = ..., score: _Optional[int] = ..., state: _Optional[_Union[PostState, str]] = ..., subreddit_id: _Optional[str] = ...) -> None: ...

class CreatePostResponse(_message.Message):
    __slots__ = ["post_created"]
    POST_CREATED_FIELD_NUMBER: _ClassVar[int]
    post_created: Post
    def __init__(self, post_created: _Optional[_Union[Post, _Mapping]] = ...) -> None: ...

class UpvotePostRequest(_message.Message):
    __slots__ = ["post_id"]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: int
    def __init__(self, post_id: _Optional[int] = ...) -> None: ...

class UpvotePostResponse(_message.Message):
    __slots__ = ["newScore"]
    NEWSCORE_FIELD_NUMBER: _ClassVar[int]
    newScore: int
    def __init__(self, newScore: _Optional[int] = ...) -> None: ...

class DownvotePostRequest(_message.Message):
    __slots__ = ["post_id"]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: int
    def __init__(self, post_id: _Optional[int] = ...) -> None: ...

class DownvotePostResponse(_message.Message):
    __slots__ = ["newScore"]
    NEWSCORE_FIELD_NUMBER: _ClassVar[int]
    newScore: int
    def __init__(self, newScore: _Optional[int] = ...) -> None: ...

class RetrievePostRequest(_message.Message):
    __slots__ = ["post_id"]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: int
    def __init__(self, post_id: _Optional[int] = ...) -> None: ...

class RetrievePostResponse(_message.Message):
    __slots__ = ["title", "text", "image_url", "video_url", "author", "score", "state", "publication_date", "subreddit_id"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    SUBREDDIT_ID_FIELD_NUMBER: _ClassVar[int]
    title: str
    text: str
    image_url: str
    video_url: str
    author: User
    score: int
    state: PostState
    publication_date: str
    subreddit_id: str
    def __init__(self, title: _Optional[str] = ..., text: _Optional[str] = ..., image_url: _Optional[str] = ..., video_url: _Optional[str] = ..., author: _Optional[_Union[User, _Mapping]] = ..., score: _Optional[int] = ..., state: _Optional[_Union[PostState, str]] = ..., publication_date: _Optional[str] = ..., subreddit_id: _Optional[str] = ...) -> None: ...

class CreateCommentRequest(_message.Message):
    __slots__ = ["author", "parent_post_id", "parent_comment_id", "state", "content"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    PARENT_POST_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    author: User
    parent_post_id: int
    parent_comment_id: int
    state: CommentState
    content: str
    def __init__(self, author: _Optional[_Union[User, _Mapping]] = ..., parent_post_id: _Optional[int] = ..., parent_comment_id: _Optional[int] = ..., state: _Optional[_Union[CommentState, str]] = ..., content: _Optional[str] = ...) -> None: ...

class CreateCommentResponse(_message.Message):
    __slots__ = ["createdComment"]
    CREATEDCOMMENT_FIELD_NUMBER: _ClassVar[int]
    createdComment: Comment
    def __init__(self, createdComment: _Optional[_Union[Comment, _Mapping]] = ...) -> None: ...

class UpvoteCommentRequest(_message.Message):
    __slots__ = ["comment_id"]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    comment_id: int
    def __init__(self, comment_id: _Optional[int] = ...) -> None: ...

class UpvoteCommentResponse(_message.Message):
    __slots__ = ["newScore"]
    NEWSCORE_FIELD_NUMBER: _ClassVar[int]
    newScore: int
    def __init__(self, newScore: _Optional[int] = ...) -> None: ...

class DownvoteCommentRequest(_message.Message):
    __slots__ = ["comment_id"]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    comment_id: int
    def __init__(self, comment_id: _Optional[int] = ...) -> None: ...

class DownvoteCommentResponse(_message.Message):
    __slots__ = ["newScore"]
    NEWSCORE_FIELD_NUMBER: _ClassVar[int]
    newScore: int
    def __init__(self, newScore: _Optional[int] = ...) -> None: ...

class MostUpvotedCommentsRequest(_message.Message):
    __slots__ = ["numberOfComments", "post_id"]
    NUMBEROFCOMMENTS_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    numberOfComments: int
    post_id: int
    def __init__(self, numberOfComments: _Optional[int] = ..., post_id: _Optional[int] = ...) -> None: ...

class MostUpvotedCommentsResponse(_message.Message):
    __slots__ = ["comments"]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    comments: _containers.RepeatedCompositeFieldContainer[Comment]
    def __init__(self, comments: _Optional[_Iterable[_Union[Comment, _Mapping]]] = ...) -> None: ...

class ExpandCommentBranchRequest(_message.Message):
    __slots__ = ["numberOfComments", "commentId"]
    NUMBEROFCOMMENTS_FIELD_NUMBER: _ClassVar[int]
    COMMENTID_FIELD_NUMBER: _ClassVar[int]
    numberOfComments: int
    commentId: int
    def __init__(self, numberOfComments: _Optional[int] = ..., commentId: _Optional[int] = ...) -> None: ...

class ExpandCommentBranchResponse(_message.Message):
    __slots__ = ["expandedComments"]
    EXPANDEDCOMMENTS_FIELD_NUMBER: _ClassVar[int]
    expandedComments: _containers.RepeatedCompositeFieldContainer[Comment]
    def __init__(self, expandedComments: _Optional[_Iterable[_Union[Comment, _Mapping]]] = ...) -> None: ...

class MonitorUpdatesRequest(_message.Message):
    __slots__ = ["originalPostID", "addedCommentID"]
    ORIGINALPOSTID_FIELD_NUMBER: _ClassVar[int]
    ADDEDCOMMENTID_FIELD_NUMBER: _ClassVar[int]
    originalPostID: int
    addedCommentID: int
    def __init__(self, originalPostID: _Optional[int] = ..., addedCommentID: _Optional[int] = ...) -> None: ...

class MonitorUpdatesResponse(_message.Message):
    __slots__ = ["postScore", "postID", "commentScores"]
    class CommentScoresEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    POSTSCORE_FIELD_NUMBER: _ClassVar[int]
    POSTID_FIELD_NUMBER: _ClassVar[int]
    COMMENTSCORES_FIELD_NUMBER: _ClassVar[int]
    postScore: int
    postID: int
    commentScores: _containers.ScalarMap[int, int]
    def __init__(self, postScore: _Optional[int] = ..., postID: _Optional[int] = ..., commentScores: _Optional[_Mapping[int, int]] = ...) -> None: ...
