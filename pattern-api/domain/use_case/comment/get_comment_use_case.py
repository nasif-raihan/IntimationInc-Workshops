from dataclasses import dataclass

from domain.model import Comment
from domain.repository import CommentRepository


@dataclass
class GetCommentUseCase:
    repository: CommentRepository

    def invoke(self, comment_id: int, title: str, username: str) -> Comment:
        return self.repository.get_comment(comment_id, title, username)

    def all(self, title: str, username: str) -> list[Comment]:
        return self.repository.get_comments(title, username)
