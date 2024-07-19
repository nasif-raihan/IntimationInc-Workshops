from blog.models import BlogPost as DBPost, PostScore as DBPostScore
from domain.model import PostScore, BlogPost
from domain.repository import PostScoreRepository


class DBPostScoreRepository(PostScoreRepository):
    def add_reputation(self, post_score: PostScore) -> PostScore:
        try:
            db_post_score = DBPostScore.objects.filter(
                post__title=post_score.post.title
            )
            db_post_score.reputation = post_score.reputation
            db_post_score.save()
            return self.to_post_score(db_post_score)
        except DBPostScore.DoesNotExist:
            db_post = DBPost.objects.get(title=post_score.post.title)
            db_post_score = DBPostScore(reputation=post_score.reputation, post=db_post)
            return self.to_post_score(db_post_score)
        except DBPost.DoesNotExist:
            raise RuntimeError("No such blog post is found!")

    def get_score(self, title: str) -> PostScore | None:
        try:
            db_post_score = DBPostScore.objects.filter(post__title=title)
            return self.to_post_score(db_post_score)
        except DBPostScore.DoesNotExist:
            return None

    def increase_reputation(self, title: str) -> PostScore:
        try:
            db_post_score = DBPostScore.objects.filter(post__title=title)
            db_post_score.reputation += 1
            db_post_score.save()
            return self.to_post_score(db_post_score)
        except DBPostScore.DoesNotExist:
            post_score = self.get_score(title)
            return self.add_reputation(post_score)

    def decrease_reputation(self, title: str) -> PostScore:
        try:
            db_post_score = DBPostScore.objects.filter(post__title=title)
            db_post_score.reputation -= 1
            db_post_score.save()
            return self.to_post_score(db_post_score)
        except DBPostScore.DoesNotExist:
            db_post = DBPost.objects.get(title)
            db_post_score = DBPostScore(reputation=-1, post=db_post)
            db_post_score.save()
            return self.to_post_score(db_post_score)
        except DBPost.DoesNotExist:
            raise RuntimeError("No such blog post is found!")

    @classmethod
    def to_blog_post(cls, db_blog_post: DBPost) -> BlogPost:
        return BlogPost(
            title=db_blog_post.title,
            content=db_blog_post.content,
            created_at=db_blog_post.created_at,
            updated_at=db_blog_post.updated_at,
            author=db_blog_post.author,
        )

    @classmethod
    def to_post_score(cls, db_post_score: DBPostScore) -> PostScore:
        blog_post = cls.to_blog_post(db_post_score.post)
        return PostScore(reputation=db_post_score.reputation, post=blog_post)
