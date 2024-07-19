from dataclasses import dataclass

from domain.model import Review
from domain.repository import ReviewRepository


@dataclass
class UpdateReviewUseCase:
    repository: ReviewRepository

    def invoke(self, review: Review) -> Review:
        return self.repository.update_review(review)
