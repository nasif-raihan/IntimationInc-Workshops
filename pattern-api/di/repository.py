from typing import Self

from data.repository import DBUserRepository, DBBlogRepository
from domain.repository import UserRepository, BlogRepository


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
    def blog_repository(self) -> BlogRepository:
        return DBBlogRepository()
