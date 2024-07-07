from dataclasses import dataclass

from domain.model import BlogPost
from domain.repository import BlogPostRepository


@dataclass
class GetBlogPostUseCase:
    blog_post_repository: BlogPostRepository

    def invoke(self, title: str, author_username: str) -> BlogPost | None:
        return self.blog_post_repository.get_blog_post(title, author_username)

    def all(self) -> list[BlogPost]:
        return self.blog_post_repository.get_all_blog_posts()
