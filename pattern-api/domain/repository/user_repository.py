from abc import ABC, abstractmethod

from blog.models import User


class UserRepository(ABC):
    @abstractmethod
    def get_user_by_username(self, username: str) -> User:
        raise NotImplementedError("Implement get_user_by_username method")

    @abstractmethod
    def get_all_users(self) -> list:
        raise NotImplementedError("Implement get_all_users method")

    @abstractmethod
    def add_user(self, user: User) -> User:
        raise NotImplementedError("Implement add_user method")

    @abstractmethod
    def update_user(self, user: User) -> User:
        raise NotImplementedError("Implement update_user method")

    @abstractmethod
    def delete_user(self, username: str) -> bool:
        raise NotImplementedError("Implement delete_user method")
