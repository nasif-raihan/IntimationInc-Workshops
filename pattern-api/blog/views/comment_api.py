import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from di.use_case import CommentUseCase, PostUseCase, UserUseCase
from domain.model import Comment
from ..serializers import CommentSerializer


class CommentAPI(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__post_use_cases = PostUseCase()
        self.__user_use_cases = UserUseCase()
        self.__comment_use_cases = CommentUseCase()

    def get(self, request) -> Response:
        title = request.data.get("title")
        username = request.data.get("username")

        if not all((title, username)):
            return Response(
                data={"message": "Invalid request payload"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        comments = self.__comment_use_cases.get_comment.all(title, username)

        return Response(
            data={"title": title, "username": username, "comments": comments},
            status=status.HTTP_200_OK,
        )

    def post(self, request) -> Response:
        serializer = CommentSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                data={"message": "Invalid request payload"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        title = serializer.data.get("title")
        username = serializer.data.get("username")
        text = serializer.data.get("text")

        post = self.__post_use_cases.get_blog_post.invoke(title, username)
        user = self.__user_use_cases.get_user.invoke(username)
        if not all((user, post)):
            return Response(data={"message": "Invalid request payload"}, status=status.HTTP_400_BAD_REQUEST)

        comment = self.__comment_use_cases.add_comment.invoke(
            comment=Comment(post, user, text)
        )
        return Response(
            data={
                "title": comment.post.title,
                "username": comment.author.username,
                "text": comment.text,
                "comment_id": comment.comment_id,
                "created_at": comment.created_at,
                "updated_at": comment.updated_at,
            },
            status=status.HTTP_201_CREATED,
        )

    def put(self, request) -> Response:
        serializer = CommentSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                data={"message": "Invalid request payload"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        title = serializer.data.get("title")
        username = serializer.data.get("username")
        text = serializer.data.get("text")

        post = self.__post_use_cases.get_blog_post.invoke(title, username)
        user = self.__user_use_cases.get_user.invoke(username)
        if not all((user, post)):
            return Response(data={"message": "Invalid request payload"}, status=status.HTTP_400_BAD_REQUEST)

        comment = self.__comment_use_cases.update_comment.invoke(
            comment=Comment(post, user, text)
        )
        return Response(
            data={
                "title": comment.post.title,
                "username": comment.author.username,
                "text": comment.text,
                "comment_id": comment.comment_id,
                "created_at": comment.created_at,
                "updated_at": comment.updated_at,
            },
            status=status.HTTP_200_OK,
        )

    def delete(self, request) -> Response:
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return Response(data={"message": "Invalid JSON payload"}, status=status.HTTP_400_BAD_REQUEST)

        title = data.get("title")
        username = data.get("username")
        comment_id = data.get("comment_id")
        if not all((comment_id, title, username)):
            return Response(data={"message": "Invalid request payload"}, status=status.HTTP_400_BAD_REQUEST)

        success = self.__comment_use_cases.delete_comment.invoke(
            comment_id, title, username
        )
        if success:
            message = "Successfully deleted the comment!"
        else:
            message = "No comment found against the provided info."

        return Response(
            data={"success": success, "message": message}, status=status.HTTP_200_OK
        )
