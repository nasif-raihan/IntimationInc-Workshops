from dataclasses import dataclass
from datetime import datetime

from .user import User


@dataclass
class Blog:
    title: str
    content: str
    created_at: datetime
    last_modified: datetime
    author: User
