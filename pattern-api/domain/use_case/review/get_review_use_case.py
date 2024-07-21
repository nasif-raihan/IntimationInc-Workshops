from dataclasses import dataclass

from domain.model import Review
from domain.repository import ReviewRepository


@dataclass
class GetReviewUseCase:
    repository: ReviewRepository

    def invoke(self, post_title: str, author_username: str, review_id: int) -> Review:
        return self.repository.get_review(post_title, author_username, review_id)

    def all(self, post_title: str) -> list[Review]:
        return self.repository.get_all_reviews(post_title)
