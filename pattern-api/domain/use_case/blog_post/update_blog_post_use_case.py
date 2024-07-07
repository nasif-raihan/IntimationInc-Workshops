from dataclasses import dataclass

from domain.model import BlogPost
from domain.repository import BlogPostRepository


@dataclass
class UpdateBlogPostUseCase:
    blog_post_repository: BlogPostRepository

    def invoke(self, blog: BlogPost) -> BlogPost:
        return self.blog_post_repository.update_blog_post(blog)
