from abc import ABC, abstractmethod

from domain.model import Comment


class CommentRepository(ABC):
    @abstractmethod
    def get_comment(self, comment_id: int) -> Comment | None:
        raise NotImplementedError("Implement get_comment method")

    @abstractmethod
    def get_comments(self, title: str, username: str) -> list[Comment]:
        raise NotImplementedError("Implement get_comments method")

    @abstractmethod
    def make_comment(self, comment: Comment) -> Comment:
        raise NotImplementedError("Implement make comment method")

    @abstractmethod
    def update_comment(self, comment: Comment) -> Comment:
        raise NotImplementedError("Implement update_comment method")

    @abstractmethod
    def delete_comment(self, comment_id: int) -> bool:
        raise NotImplementedError("Implement delete_comment method")
