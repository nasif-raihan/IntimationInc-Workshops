from dataclasses import dataclass

from domain.model import Blog
from domain.repository import BlogRepository


@dataclass
class UpdateBlogUseCase:
    blog_repository: BlogRepository

    def invoke(self, blog: Blog) -> Blog:
        return self.blog_repository.update_blog(blog)
