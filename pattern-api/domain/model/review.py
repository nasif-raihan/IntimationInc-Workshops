from dataclasses import dataclass

from .blog_post import BlogPost
from .user import User


@dataclass
class Review:
    title: str
    rating: float
    content: str
    pros: str
    cons: str
    idea: str
    recommendation: str
    author_feedback: str
    post: BlogPost
    reviewer: User
    review_id: int = None
