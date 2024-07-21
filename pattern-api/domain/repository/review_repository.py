from abc import ABC, abstractmethod

from ..model import Review


class ReviewRepository(ABC):
    @abstractmethod
    def add_review(self, review: Review) -> Review:
        raise NotImplementedError("Implement add_review method")

    @abstractmethod
    def get_all_reviews(self, post_title: str, author_username: str) -> list[Review]:
        raise NotImplementedError("Implement get_all_reviews method")

    @abstractmethod
    def get_review(self, post_title: str, author_username: str,  review_id: int) -> Review | None:
        raise NotImplementedError("Implement get_review method")

    @abstractmethod
    def update_review(self, review: Review) -> Review:
        raise NotImplementedError("Implement update_review method")

    @abstractmethod
    def delete_review(self, post_title: str, author_username: str, review_id: int) -> bool:
        raise NotImplementedError("Implement delete_review method")
