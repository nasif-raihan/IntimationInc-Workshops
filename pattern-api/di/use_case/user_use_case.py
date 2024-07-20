from domain.use_case.user import (
    AddUserUseCase,
    DeleteUserUseCase,
    GetUserUseCase,
    UpdateUserUseCase,
)
from di.repository import Repository


class UserUseCase:
    def __init__(self):
        self._repository = Repository.get_instance()

    @property
    def add_user(self) -> AddUserUseCase:
        return AddUserUseCase(user_repository=self._repository.user_repository)

    @property
    def get_user(self) -> GetUserUseCase:
        return GetUserUseCase(user_repository=self._repository.user_repository)

    @property
    def update_user(self) -> UpdateUserUseCase:
        return UpdateUserUseCase(user_repository=self._repository.user_repository)

    @property
    def delete_user(self) -> DeleteUserUseCase:
        return DeleteUserUseCase(user_repository=self._repository.user_repository)
