from blog.models import Review as DBReview, BlogPost as DBPost, User as DBUser
from domain.model import Review, BlogPost, User
from domain.repository import ReviewRepository


class DBReviewRepository(ReviewRepository):
    def add_review(self, review: Review) -> Review:
        try:
            DBReview.objects.get(
                title=review.title, reviewer__username=review.reviewer.username, post__title=review.post.title
            )
            return self.update_review(review)
        except DBReview.DoesNotExist:
            try:
                db_user = DBUser.objects.get(username=review.reviewer.username)
            except DBUser.DoesNotExist:
                raise RuntimeError("No such user exist as reviewer")

            try:
                db_post = DBPost.objects.get(title=review.post.title, username=review.post.author.username)
            except DBPost.DoesNotExist:
                raise RuntimeError("No such blog post exist to review")

            db_review = DBReview(
                title=review.title,
                rating=review.rating,
                content=review.content,
                pros=review.pros,
                cons=review.cons,
                idea=review.idea,
                recommendation=review.recommendation,
                author_feedback=review.author_feedback,
                post=db_post,
                reviewer=db_user,
            )
            db_review.save()
            return self.to_review(db_review)

    def get_all_reviews(self, post_title: str) -> list[Review]:
        try:
            db_reviews = DBReview.objects.filter(post__title=post_title)
            return [self.to_review(db_review) for db_review in db_reviews]
        except DBReview.DoesNotExist:
            return []

    def get_review(self, post_title: str, review_id: int) -> Review | None:
        try:
            db_review = DBReview.objects.get(id=review_id, post__title=post_title)
            return self.to_review(db_review)
        except DBReview.DoesNotExist:
            return None

    def update_review(self, review: Review) -> Review:
        try:
            db_review = DBReview.objects.get(id=review.review_id, post__title=review.post.title)
            db_review.title = review.title
            db_review.rating = review.rating
            db_review.content = review.content
            db_review.pros = review.pros
            db_review.cons = review.cons
            db_review.idea = review.idea
            db_review.recommendation = review.recommendation
            db_review.author_feedback = review.author_feedback
            db_review.save()
            return self.to_review(db_review)
        except DBReview.DoesNotExist:
            return self.add_review(review)

    def delete_review(self, post_title: str, review_id: int) -> bool:
        try:
            db_review = DBReview.objects.get(id=review_id, post__title=post_title)
            db_review.delete()
            return True
        except DBReview.DoesNotExist:
            return False

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
    def to_user(cls, db_user: DBUser) -> User:
        return User(
            email=db_user.email,
            username=db_user.username,
            is_active=db_user.is_active,
            is_staff=db_user.is_staff,
            is_admin=db_user.is_admin,
            created_at=db_user.created_at,
            updated_at=db_user.updated_at,
        )

    @classmethod
    def to_review(cls, db_review: DBReview) -> Review:
        post = cls.to_blog_post(db_review.post)
        user = cls.to_user(db_review.reviewer)
        return Review(
            review_id=db_review.id,
            title=db_review.title,
            rating=db_review.rating,
            content=db_review.content,
            pros=db_review.pros,
            cons=db_review.cons,
            idea=db_review.idea,
            recommendation=db_review.recommendation,
            author_feedback=db_review.author_feedback,
            post=post,
            reviewer=user,
        )
