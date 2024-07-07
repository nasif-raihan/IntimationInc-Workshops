from django.contrib import admin

from .models import Comment, BlogPost, User


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_at", "updated_at", "author")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "username",
        "is_active",
        "is_staff",
        "is_admin",
        "created_at",
        "updated_at",
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "comment", "created_at", "updated_at")
