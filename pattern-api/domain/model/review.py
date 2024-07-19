from dataclasses import dataclass

from .blog_post import BlogPost


@dataclass
class Review:
    review_id: int
    title: str
    rating: float
    content: str
    pros: str
    cons: str
    idea: str
    recommendation: str
    author_feedback: str
    post: BlogPost
