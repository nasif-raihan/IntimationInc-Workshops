from dataclasses import dataclass

from domain.model import User
from domain.repository import UserRepository


@dataclass
class AddUserUseCase:
    user_repository: UserRepository

    def invoke(self, user: User) -> User:
        return self.user_repository.add_user(user)
