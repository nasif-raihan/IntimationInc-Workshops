from django.contrib import admin

from .models import Comment, BlogPost, User, PostScore, UserScore, Review, Video


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


@admin.register(PostScore)
class PostScoreAdmin(admin.ModelAdmin):
    list_display = ("reputation", "post")


@admin.register(UserScore)
class UserScoreAdmin(admin.ModelAdmin):
    list_display = ("reputation", "user")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("title", "rating", "post", "reviewer", "created_at", "updated_at")


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("video_id", "url")
