from dataclasses import dataclass
from datetime import datetime

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
    created_at: datetime = None
    updated_at: datetime = datetime.now()
