from typing import Self

from blog.models import BlogPost as DBBlogPost, Comment as DBComment, PostScore as DBPostScore, Review as DBReview, \
    User as DBUser, UserScore as DBUserScore
from domain.model import BlogPost, Comment, PostScore, Review, User, UserScore


class Mapper:
    __instance = None

    def __init__(self):
        if self.__instance:
            raise RuntimeError("An instance of Mapper is already running")

    @classmethod
    def get_instance(cls) -> Self:
        if cls.__instance is None:
            cls.__instance = Mapper()
        return cls.__instance

    @classmethod
    def to_blog_post(cls, db_blog_post: DBBlogPost) -> BlogPost:
        return BlogPost(
            title=db_blog_post.title,
            content=db_blog_post.content,
            created_at=db_blog_post.created_at,
            updated_at=db_blog_post.updated_at,
            author=db_blog_post.author,
        )

    @classmethod
    def to_user(cls, db_user: DBUser) -> User:
        return User(
            email=db_user.email,
            username=db_user.username,
            is_active=db_user.is_active,
            is_staff=db_user.is_staff,
            is_admin=db_user.is_admin,
            created_at=db_user.created_at,
            updated_at=db_user.updated_at,
        )

    @classmethod
    def to_comment(cls, db_comment: DBComment) -> Comment:
        return Comment(
            comment_id=db_comment.id,
            post=db_comment.post,
            author=db_comment.author,
            text=db_comment.text,
            created_at=db_comment.created_at,
        )

    @classmethod
    def to_post_score(cls, db_post_score: DBPostScore) -> PostScore:
        blog_post = cls.to_blog_post(db_post_score.post)
        return PostScore(reputation=db_post_score.reputation, post=blog_post)

    @classmethod
    def to_user_score(cls, db_user_score: DBUserScore) -> UserScore:
        user = cls.to_user(db_user_score.user)
        return UserScore(reputation=db_user_score.reputation, user=user)

    @classmethod
    def to_review(cls, db_review: DBReview) -> Review:
        post = cls.to_blog_post(db_review.post)
        user = cls.to_user(db_review.reviewer)
        return Review(
            review_id=db_review.id,
            title=db_review.title,
            rating=db_review.rating,
            content=db_review.content,
            pros=db_review.pros,
            cons=db_review.cons,
            idea=db_review.idea,
            recommendation=db_review.recommendation,
            author_feedback=db_review.author_feedback,
            post=post,
            reviewer=user,
            created_at=db_review.created_at,
            updated_at=db_review.updated_at
        )
