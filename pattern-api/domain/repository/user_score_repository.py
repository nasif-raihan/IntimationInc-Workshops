from abc import ABC, abstractmethod

from ..model import UserScore


class UserScoreRepository(ABC):
    @abstractmethod
    def add_reputation(self, user_score: UserScore) -> UserScore:
        raise NotImplementedError("Implement add_score method")

    @abstractmethod
    def get_score(self, username: str) -> UserScore | None:
        raise NotImplementedError("Implement get_score method")

    @abstractmethod
    def increase_reputation(self, username: str) -> UserScore:
        raise NotImplementedError("Implement increase_reputation method")

    @abstractmethod
    def decrease_reputation(self, username: str) -> UserScore:
        raise NotImplementedError("Implement decrease_reputation method")
