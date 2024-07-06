from blog.models import Blog as DBBlog
from domain.model import Blog
from domain.repository import BlogRepository


class DBBlogRepository(BlogRepository):
    def get_blog(self, title: str, author_username: str) -> Blog | None:
        try:
            db_blog = DBBlog.objects.get(title=title, author__username=author_username)
        except DBBlog.DoesNotExist:
            return None
        return self.to_blog(db_blog)

    def get_all_blogs(self) -> list[Blog]:
        db_blogs = DBBlog.objects.all()
        if len(db_blogs):
            return [self.to_blog(db_blog) for db_blog in db_blogs]
        return []

    def add_blog(self, blog: Blog) -> Blog:
        try:
            DBBlog.objects.get(title=blog.title, author__username=blog.author.username)
        except DBBlog.DoesNotExist:
            db_blog = DBBlog(title=blog.title, content=blog.content, author=blog.author)
            db_blog.save()
            return self.to_blog(db_blog)
        return self.update_blog(blog)

    def update_blog(self, blog: Blog) -> Blog:
        try:
            db_blog = DBBlog.objects.get(
                title=blog.title, author__username=blog.author.username
            )
        except DBBlog.DoesNotExist:
            raise RuntimeError(
                f"The blog titled {blog.title} authored by {blog.author} is not found"
            )

        db_blog.title = blog.title
        db_blog.content = blog.content
        db_blog.save()

        return self.to_blog(db_blog)

    def delete_blog(self, title: str, author_username: str) -> bool:
        try:
            db_blog = DBBlog.objects.get(title=title, author__username=author_username)
            db_blog.delete()
            return True
        except DBBlog.DoesNotExist:
            return False

    @classmethod
    def to_blog(cls, db_blog: DBBlog) -> Blog:
        return Blog(
            title=db_blog.title,
            content=db_blog.content,
            created_at=db_blog.created_at,
            updated_at=db_blog.updated_at,
            author=db_blog.author,
        )
