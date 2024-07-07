from abc import ABC, abstractmethod

from domain.model.blog_post import BlogPost


class BlogPostRepository(ABC):
    @abstractmethod
    def get_blog_post(self, title: str, author_username: str) -> BlogPost | None:
        raise NotImplementedError("Implement get_blog_post method")

    @abstractmethod
    def get_all_blog_posts(self) -> list[BlogPost]:
        raise NotImplementedError("Implement get_blog_post_by_id method")

    @abstractmethod
    def add_blog_post(self, blog_post: BlogPost) -> BlogPost:
        raise NotImplementedError("Implement add_blog_post method")

    @abstractmethod
    def update_blog_post(self, blog_post: BlogPost) -> BlogPost:
        raise NotImplementedError("Implement update_blog_post method")

    @abstractmethod
    def delete_blog_post(self, title: str, author_username: str) -> bool:
        raise NotImplementedError("Implement delete_blog_post method")
