from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import BlogPostAPI, UserAPI, ReviewAPI, CommentAPI, ScoreAPI, VideoAPI

urlpatterns = [
    path("blog/", csrf_exempt(BlogPostAPI.as_view()), name="blog"),
    path("user/", csrf_exempt(UserAPI.as_view()), name="user"),
    path("comment/", csrf_exempt(CommentAPI.as_view()), name="comment"),
    path("review/", csrf_exempt(ReviewAPI.as_view()), name="review"),
    path("score/", csrf_exempt(ScoreAPI.as_view()), name="score"),
    path("v1/video/", csrf_exempt(VideoAPI.as_view()), name="video-v1"),
]
