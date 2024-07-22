from domain.use_case.review import (
    AddReviewUseCase,
    DeleteReviewUseCase,
    GetReviewUseCase,
    UpdateReviewUseCase,
)
from di.repository import Repository


class ReviewUseCase:
    def __init__(self):
        self.__repository = Repository.get_instance()

    @property
    def add_review(self) -> AddReviewUseCase:
        return AddReviewUseCase(self.__repository.review_repository)

    @property
    def get_review(self) -> GetReviewUseCase:
        return GetReviewUseCase(self.__repository.review_repository)

    @property
    def update_review(self) -> UpdateReviewUseCase:
        return UpdateReviewUseCase(self.__repository.review_repository)

    @property
    def delete_review(self) -> DeleteReviewUseCase:
        return DeleteReviewUseCase(self.__repository.review_repository)
