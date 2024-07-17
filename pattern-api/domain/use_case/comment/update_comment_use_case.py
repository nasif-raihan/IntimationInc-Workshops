from dataclasses import dataclass

from domain.model import Comment
from domain.repository import CommentRepository


@dataclass
class UpdateCommentUseCase:
    repository: CommentRepository

    def invoke(self, comment: Comment) -> Comment:
        return self.repository.update_comment(comment)
