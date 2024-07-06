from django.contrib import admin

from .models import Blog, User


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
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
