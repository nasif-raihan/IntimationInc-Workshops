from dataclasses import dataclass

from domain.repository import BlogRepository


@dataclass
class DeleteBlogUseCase:
    blog_repository: BlogRepository

    def invoke(self, title: str, author_username: str) -> bool:
        return self.blog_repository.delete_blog(title, author_username)
