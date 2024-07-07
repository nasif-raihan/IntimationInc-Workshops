from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.serializers import BlogPostSerializer
from di.use_case import UseCase
from domain.model import BlogPost


class BlogPostAPI(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._use_cases = UseCase()

    def get(self, request) -> Response:
        response = request.data
        title = response.get("title")
        author_username = response.get("author_username")

        if not all((title, author_username)):
            return Response(
                data={"message": "Invalid request payload"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        blog_post = self._use_cases.get_blog_post.invoke(title, author_username)
        user = self._use_cases.get_user.invoke(author_username)

        return Response(
            data={
                "title": blog_post.title,
                "content": blog_post.content,
                "createdAt": blog_post.created_at,
                "updatedAt": blog_post.updated_at,
                "author": {
                    "email": user.email,
                    "username": user.username,
                },
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request) -> Response:
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.data.get("title")
            content = serializer.data.get("content")
            author = serializer.data.get("author")
            blog_post = self._use_cases.add_blog_post.invoke(
                blog=BlogPost(title=title, content=content, author=author)
            )
            return Response(
                data={
                    "title": blog_post.title,
                    "content": blog_post.content,
                    "createdAt": blog_post.created_at,
                    "updatedAt": blog_post.updated_at,
                    "author": {
                        "email": author.get("email"),
                        "username": author.get("username"),
                    },
                },
                status=status.HTTP_201_CREATED,
            )

    def put(self, request) -> Response:
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.data.get("title")
            content = serializer.data.get("content")
            author = serializer.data.get("author")
            blog_post = self._use_cases.update_blog_post.invoke(
                blog=BlogPost(title=title, content=content, author=author)
            )
            return Response(
                data={
                    "title": blog_post.title,
                    "content": blog_post.content,
                    "createdAt": blog_post.created_at,
                    "updatedAt": blog_post.updated_at,
                    "author": {
                        "email": author.get("email"),
                        "username": author.get("username"),
                    },
                },
                status=status.HTTP_200_OK,
            )

    def delete(self, request) -> Response:
        title = request.data.get("title")
        author_username = request.data.get("author_username")
        if not all((title, author_username)):
            return Response(
                data={"message": "Invalid request payload"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        self._use_cases.delete_blog_post.invoke(title, author_username)
        return Response(
            data={
                "title": title,
                "author": author_username,
                "message": "Deleted the blog_post successfully",
            },
            status=status.HTTP_200_OK,
        )
