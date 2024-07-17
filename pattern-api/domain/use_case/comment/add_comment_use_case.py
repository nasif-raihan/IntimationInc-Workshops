from dataclasses import dataclass

from domain.model import Comment
from domain.repository import CommentRepository


@dataclass
class AddCommentUseCase:
    repository: CommentRepository

    def invoke(self, comment: Comment) -> Comment:
        return self.repository.make_comment(comment)
