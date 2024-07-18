from typing import Self

from data.repository import DBUserRepository, DBBlogPostRepository
from domain.repository import UserRepository, BlogPostRepository, CommentRepository


class Repository:
    __instance = None

    def __init__(self):
        if self.__instance:
            raise RuntimeError("An instance of Repository is already running")

    @classmethod
    def get_instance(cls) -> Self:
        if cls.__instance is None:
            cls.__instance = Repository()
        return cls.__instance

    @property
    def user_repository(self) -> UserRepository:
        return DBUserRepository()

    @property
    def blog_post_repository(self) -> BlogPostRepository:
        return DBBlogPostRepository()

    @property
    def comment_repository(self) -> CommentRepository:
        return CommentRepository()
