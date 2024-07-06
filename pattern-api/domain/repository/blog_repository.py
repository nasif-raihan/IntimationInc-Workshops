from abc import ABC, abstractmethod

from domain.model.blog import Blog


class BlogRepository(ABC):
    @abstractmethod
    def get_blog_by_id(self, blog_id: int) -> Blog | None:
        raise NotImplementedError("Implement get_blog_by_id method")

    @abstractmethod
    def get_all_blogs(self) -> list:
        raise NotImplementedError("Implement get_blog_by_id method")

    @abstractmethod
    def add_blog(self, blog: Blog) -> Blog:
        raise NotImplementedError("Implement add_blog method")

    @abstractmethod
    def update_blog(self, blog: Blog) -> Blog:
        raise NotImplementedError("Implement update_blog method")

    @abstractmethod
    def delete_blog(self, blog_id: int) -> bool:
        raise NotImplementedError("Implement delete_blog method")
