from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    email: str
    username: str
    is_active: bool = True
    is_staff: bool = False
    is_admin: bool = False
    created_at: datetime = None
    updated_at: datetime = datetime.now()
