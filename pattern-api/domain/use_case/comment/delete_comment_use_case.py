from dataclasses import dataclass

from domain.repository import CommentRepository


@dataclass
class DeleteCommentUseCase:
    repository: CommentRepository

    def invoke(self, comment_id: int, title: str, username: str) -> bool:
        return self.repository.delete_comment(comment_id, title, username)
