from dataclasses import dataclass

from domain.repository import BlogPostRepository


@dataclass
class DeleteBlogPostUseCase:
    blog_post_repository: BlogPostRepository

    def invoke(self, title: str, author_username: str) -> bool:
        return self.blog_post_repository.delete_blog_post(title, author_username)
