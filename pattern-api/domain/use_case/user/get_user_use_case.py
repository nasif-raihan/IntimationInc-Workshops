from dataclasses import dataclass

from domain.model import User
from domain.repository import UserRepository


@dataclass
class GetUserUseCase:
    user_repository: UserRepository

    def invoke(self, username: str) -> User | None:
        return self.user_repository.get_user_by_username(username)

    def all(self) -> list[User]:
        return self.user_repository.get_all_users()
