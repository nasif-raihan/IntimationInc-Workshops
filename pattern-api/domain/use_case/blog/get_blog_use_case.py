from dataclasses import dataclass

from domain.model import Blog
from domain.repository import BlogRepository


@dataclass
class GetBlogUseCase:
    blog_repository: BlogRepository

    def invoke(self, title: str, author_username: str) -> Blog | None:
        return self.blog_repository.get_blog(title, author_username)

    def all(self) -> list[Blog]:
        return self.blog_repository.get_all_blogs()
