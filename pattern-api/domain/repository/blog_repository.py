from abc import ABC, abstractmethod

from domain.model.blog import Blog


class BlogRepository(ABC):
    @abstractmethod
    def get_blog(self, title: str, author_username: str) -> Blog | None:
        raise NotImplementedError("Implement get_blog method")

    @abstractmethod
    def get_all_blogs(self) -> list[Blog]:
        raise NotImplementedError("Implement get_blog_by_id method")

    @abstractmethod
    def add_blog(self, blog: Blog) -> Blog:
        raise NotImplementedError("Implement add_blog method")

    @abstractmethod
    def update_blog(self, blog: Blog) -> Blog:
        raise NotImplementedError("Implement update_blog method")

    @abstractmethod
    def delete_blog(self, title: str, author_username: str) -> bool:
        raise NotImplementedError("Implement delete_blog method")
