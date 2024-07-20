from domain.use_case.comment import (
    AddCommentUseCase,
    GetCommentUseCase,
    UpdateCommentUseCase,
    DeleteCommentUseCase,
)
from di.repository import Repository


class CommentUseCase:
    def __init__(self):
        self.__repository = Repository()

    @property
    def add_comment(self) -> AddCommentUseCase:
        return AddCommentUseCase(self.__repository.comment_repository)

    @property
    def get_comment(self) -> GetCommentUseCase:
        return GetCommentUseCase(self.__repository.comment_repository)

    @property
    def update_comment(self) -> UpdateCommentUseCase:
        return UpdateCommentUseCase(self.__repository.comment_repository)

    @property
    def delete_comment(self) -> DeleteCommentUseCase:
        return DeleteCommentUseCase(self.__repository.comment_repository)
