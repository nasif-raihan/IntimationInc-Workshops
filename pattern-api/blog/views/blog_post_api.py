import json

from django.http import JsonResponse
from django.views import View

from di.use_case.post_use_case import PostUseCase
from domain.model import BlogPost, User
from ..forms import BlogPostForm


class BlogPostAPI(View):
    # permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._use_cases = PostUseCase()

    def get(self, request) -> JsonResponse:
        blog_posts = self._use_cases.get_blog_post.all()
        formatted_blog_posts = []
        for blog_post in blog_posts:
            user = self._use_cases.get_user.invoke(blog_post.author.username)
            formatted_blog_posts.append(
                {
                    "title": blog_post.title,
                    "content": blog_post.content,
                    "createdAt": blog_post.created_at,
                    "updatedAt": blog_post.updated_at,
                    "author": {
                        "email": user.email,
                        "username": user.username,
                    },
                }
            )
        return JsonResponse(data={"blogs": formatted_blog_posts}, status=200)

    def post(self, request) -> JsonResponse:
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse(data={"message": "Invalid JSON payload"}, status=400)

        form = BlogPostForm(data=data)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            blog_post = self._use_cases.add_blog_post.invoke(
                blog=BlogPost(
                    title=title, content=content, author=User(email, username)
                )
            )
            return JsonResponse(
                data={
                    "title": blog_post.title,
                    "content": blog_post.content,
                    "createdAt": blog_post.created_at,
                    "updatedAt": blog_post.updated_at,
                    "author": {
                        "email": blog_post.author.email,
                        "username": blog_post.author.username,
                    },
                },
                status=201,
            )
        return JsonResponse(data=form.errors, status=400)

    def put(self, request) -> JsonResponse:
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse(data={"message": "Invalid JSON payload"}, status=400)

        form = BlogPostForm(data=data)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            blog_post = self._use_cases.update_blog_post.invoke(
                blog=BlogPost(
                    title=title, content=content, author=User(email, username)
                )
            )
            return JsonResponse(
                data={
                    "title": blog_post.title,
                    "content": blog_post.content,
                    "createdAt": blog_post.created_at,
                    "updatedAt": blog_post.updated_at,
                    "author": {
                        "email": blog_post.author.email,
                        "username": blog_post.author.username,
                    },
                },
                status=200,
            )
        return JsonResponse(data=form.errors, status=400)

    def delete(self, request) -> JsonResponse:
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse(data={"message": "Invalid JSON payload"}, status=400)

        title = data.get("title")
        username = data.get("username")
        if not all((title, username)):
            return JsonResponse(data={"message": "Invalid request payload"}, status=400)

        self._use_cases.delete_blog_post.invoke(title, username)
        return JsonResponse(
            data={
                "title": title,
                "author": username,
                "message": "Deleted the blog post successfully",
            },
            status=200,
        )

    @staticmethod
    def __get_blog_post_form(data: dict) -> BlogPostForm:
        return BlogPostForm(data)
