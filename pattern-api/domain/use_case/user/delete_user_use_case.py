from dataclasses import dataclass

from domain.repository import UserRepository


@dataclass
class DeleteUserUseCase:
    user_repository: UserRepository

    def invoke(self, username: str) -> bool:
        return self.user_repository.delete_user(username)
