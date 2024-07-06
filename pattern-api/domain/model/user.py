from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    email: str
    username: str
    is_active: bool
    is_staff: bool
    is_admin: bool
    created_at: datetime
    updated_at: datetime
