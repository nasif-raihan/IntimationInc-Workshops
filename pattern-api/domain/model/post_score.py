from dataclasses import dataclass

from .blog_post import BlogPost


@dataclass
class PostScore:
    reputation: int
    post: BlogPost
