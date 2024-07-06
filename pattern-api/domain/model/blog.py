from dataclasses import dataclass
from datetime import datetime

from .user import User


@dataclass
class Blog:
    blog_id: int
    title: str
    content: str
    created_at: datetime
    last_modified: datetime
    created_by: User
