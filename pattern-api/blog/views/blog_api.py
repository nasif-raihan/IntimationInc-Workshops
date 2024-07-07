from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.serializers import BlogSerializer
from di.use_case import UseCase
from domain.model import Blog


class BlogAPI(APIView):
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

        blog = self._use_cases.get_blog.invoke(title, author_username)
        user = self._use_cases.get_user.invoke(author_username)

        return Response(
            data={
                "title": blog.title,
                "content": blog.content,
                "createdAt": blog.created_at,
                "updatedAt": blog.updated_at,
                "author": {
                    "email": user.email,
                    "username": user.username,
                },
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request) -> Response:
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.data.get("title")
            content = serializer.data.get("content")
            author = serializer.data.get("author")
            blog = self._use_cases.add_blog.invoke(
                blog=Blog(title=title, content=content, author=author)
            )
            return Response(
                data={
                    "title": blog.title,
                    "content": blog.content,
                    "createdAt": blog.created_at,
                    "updatedAt": blog.updated_at,
                    "author": {
                        "email": author.get("email"),
                        "username": author.get("username"),
                    },
                },
                status=status.HTTP_201_CREATED,
            )

    def put(self, request) -> Response:
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.data.get("title")
            content = serializer.data.get("content")
            author = serializer.data.get("author")
            blog = self._use_cases.update_blog.invoke(
                blog=Blog(title=title, content=content, author=author)
            )
            return Response(
                data={
                    "title": blog.title,
                    "content": blog.content,
                    "createdAt": blog.created_at,
                    "updatedAt": blog.updated_at,
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

        self._use_cases.delete_blog.invoke(title, author_username)
        return Response(
            data={
                "title": title,
                "author": author_username,
                "message": "Deleted the blog successfully",
            },
            status=status.HTTP_200_OK,
        )
