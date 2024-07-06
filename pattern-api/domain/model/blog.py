from dataclasses import dataclass
from datetime import datetime

from .user import User


@dataclass
class Blog:
    title: str
    content: str
    author: User
    created_at: datetime = None
    updated_at: datetime = datetime.now()
