from blog.models import BlogPost as DBBlogPost, User as DBUser
from domain.model import BlogPost
from domain.repository import BlogPostRepository


class DBBlogPostRepository(BlogPostRepository):
    def get_blog_post(self, title: str, author_username: str) -> BlogPost | None:
        try:
            db_blog_post = DBBlogPost.objects.get(
                title=title, author__username=author_username
            )
        except DBBlogPost.DoesNotExist:
            return None
        return self.to_blog_post(db_blog_post)

    def get_all_blog_posts(self) -> list[BlogPost]:
        db_blog_posts = DBBlogPost.objects.all()
        if len(db_blog_posts):
            return [self.to_blog_post(db_blog_post) for db_blog_post in db_blog_posts]
        return []

    def add_blog_post(self, blog_post: BlogPost) -> BlogPost:
        try:
            DBBlogPost.objects.get(
                title=blog_post.title, author__username=blog_post.author.username
            )
        except DBBlogPost.DoesNotExist:
            db_user = DBUser.objects.get(username=blog_post.author.username)
            if not db_user:
                raise RuntimeError("User not found")

            db_blog_post = DBBlogPost(
                title=blog_post.title,
                content=blog_post.content,
                author=db_user,
            )
            db_blog_post.save()
            return self.to_blog_post(db_blog_post)
        return self.update_blog_post(blog_post)

    def update_blog_post(self, blog_post: BlogPost) -> BlogPost:
        try:
            db_blog_post = DBBlogPost.objects.get(
                title=blog_post.title, author__username=blog_post.author.username
            )
        except DBBlogPost.DoesNotExist:
            raise RuntimeError(
                f"The post titled {blog_post.title} authored by {blog_post.author} is not found"
            )

        db_blog_post.title = blog_post.title
        db_blog_post.content = blog_post.content
        db_blog_post.save()

        return self.to_blog_post(db_blog_post)

    def delete_blog_post(self, title: str, author_username: str) -> bool:
        try:
            db_blog_post = DBBlogPost.objects.get(
                title=title, author__username=author_username
            )
            db_blog_post.delete()
            return True
        except DBBlogPost.DoesNotExist:
            return False

    @classmethod
    def to_blog_post(cls, db_blog_post: DBBlogPost) -> BlogPost:
        return BlogPost(
            title=db_blog_post.title,
            content=db_blog_post.content,
            created_at=db_blog_post.created_at,
            updated_at=db_blog_post.updated_at,
            author=db_blog_post.author,
        )
