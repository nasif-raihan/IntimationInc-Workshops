from abc import ABC, abstractmethod

from ..model import PostScore


class PostScoreRepository(ABC):
    @abstractmethod
    def add_reputation(self, post_score: PostScore) -> PostScore:
        raise NotImplementedError("Implement add_score method")

    @abstractmethod
    def get_score(self, title: str) -> PostScore | None:
        raise NotImplementedError("Implement get_score method")

    @abstractmethod
    def increase_reputation(self, title: str) -> PostScore:
        raise NotImplementedError("Implement increase_reputation method")

    @abstractmethod
    def decrease_reputation(self, title: str) -> PostScore:
        raise NotImplementedError("Implement decrease_reputation method")
