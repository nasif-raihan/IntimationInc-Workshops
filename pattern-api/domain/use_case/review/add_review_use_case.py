from dataclasses import dataclass

from domain.model import Review
from domain.repository import ReviewRepository


@dataclass
class AddReviewUseCase:
    repository: ReviewRepository

    def invoke(self, review: Review) -> Review:
        return self.repository.add_review(review)
