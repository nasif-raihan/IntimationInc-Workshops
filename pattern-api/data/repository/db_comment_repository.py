from blog.models import Comment as DBComment
from domain.model import Comment
from domain.repository import CommentRepository


class DBCommentRepository(CommentRepository):
    def get_comment(self, comment_id: int) -> Comment | None:
        try:
            db_comment = DBComment.objects.get(id=comment_id)
        except DBComment.DoesNotExist:
            return None
        return self.to_comment(db_comment)

    def get_comments(self, title: str, username: str) -> list[Comment]:
        try:
            db_comments = DBComment.objects.filter(
                post__title=title, author__username=username
            )
        except DBComment.DoesNotExist:
            return []
        return [self.to_comment(db_comment) for db_comment in db_comments]

    def make_comment(self, comment: Comment) -> Comment:
        db_comment = DBComment(
            post=comment.post, author=comment.author, text=comment.text
        )
        return self.to_comment(db_comment)

    def update_comment(self, comment: Comment) -> Comment:
        db_comment = DBComment.objects.get(id=comment.comment_id)

        if db_comment is None:
            return self.make_comment(comment)

        db_comment.text = comment.text
        db_comment.save()

        return self.to_comment(db_comment)

    def delete_comment(self, comment_id: int) -> bool:
        db_comment = DBComment.objects.get(id=comment_id)

        if db_comment:
            db_comment.delete()
            return True
        return False

    @classmethod
    def to_comment(cls, db_comment: DBComment) -> Comment:
        return Comment(
            comment_id=db_comment.id,
            post=db_comment.post,
            author=db_comment.author,
            text=db_comment.text,
            created_at=db_comment.created_at,
        )
