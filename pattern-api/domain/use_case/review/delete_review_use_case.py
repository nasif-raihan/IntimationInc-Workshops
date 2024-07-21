from dataclasses import dataclass

from domain.model import Review
from domain.repository import ReviewRepository


@dataclass
class DeleteReviewUseCase:
    repository: ReviewRepository

    def invoke(self, post_title: str, author_username: str, review_id: int) -> Review:
        return self.repository.delete_review(post_title, author_username, review_id)
