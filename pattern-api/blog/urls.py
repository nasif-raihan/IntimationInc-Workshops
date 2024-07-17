from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import BlogPostAPI, UserAPI

urlpatterns = [
    path("blog/", csrf_exempt(BlogPostAPI.as_view()), name="blog"),
    path("user/", csrf_exempt(UserAPI.as_view()), name="user"),
]
