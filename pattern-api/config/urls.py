from django.contrib import admin
from django.urls import path, include

from blog import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", views.BlogPostAPI.as_view(), name="blog"),
    path("user/", views.UserAPI.as_view(), name="user"),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
]
