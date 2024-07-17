from dataclasses import dataclass
from datetime import datetime

from .blog_post import BlogPost
from .user import User


@dataclass
class Comment:
    post: BlogPost
    author: User
    text: str
    comment_id: int = None
    created_at: datetime = None
    updated_at: datetime = datetime.now()
