from abc import ABC, abstractmethod

from ..model import Review


class ReviewRepository(ABC):
    @abstractmethod
    def add_review(self) -> Review:
        raise NotImplementedError("Implement add_review method")

    @abstractmethod
    def get_all_reviews(self) -> list[Review]:
        raise NotImplementedError("Implement get_all_reviews method")

    @abstractmethod
    def get_review(self) -> Review:
        raise NotImplementedError("Implement get_review method")

    @abstractmethod
    def update_review(self) -> Review:
        raise NotImplementedError("Implement update_review method")

    @abstractmethod
    def delete_review(self) -> Review:
        raise NotImplementedError("Implement delete_review method")
