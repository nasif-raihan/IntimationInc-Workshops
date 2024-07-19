from dataclasses import dataclass

from .user import User


@dataclass
class UserScore:
    reputation: int
    user: User
