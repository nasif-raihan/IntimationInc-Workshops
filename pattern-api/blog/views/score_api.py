import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from di.use_case import ScoreUseCase, UserUseCase
from ..serializers import ScoreSerializer


class ScoreAPI(APIView):
    def __init__(self):
        self.__score_use_case = ScoreUseCase()
        self.__user_use_case = UserUseCase()

    def get(self, request) -> Response:
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return Response(data={"message": "Invalid JSON payload"}, status=status.HTTP_400_BAD_REQUEST)

        title = data.get("title")
        username = data.get("username")
        if not all((title, username)):
            return Response(data={"message": "Invalid request payload"}, status=status.HTTP_400_BAD_REQUEST)

        post_reputation = self.__score_use_case.get_post_reputation.invoke(title, username)
        user_reputation = self.__score_use_case.get_user_reputation.invoke(username)

        return Response(
            data={
                "postReputation": {
                    "postTitle": post_reputation.post.title,
                    "reputation": post_reputation.reputation
                },
                "userReputation": {
                    "username": user_reputation.user.username,
                    "reputation": user_reputation.reputation
                }
            }, status=status.HTTP_200_OK
        )

    def post(self, request) -> Response:
        serializer = ScoreSerializer(request.data)

        if not serializer.is_valid():
            return Response(
                data={"message": "Invalid request payload"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        title = serializer.data.get("blog_post_title")
        author_username = serializer.data.get("author_username")
        reviewer_username = serializer.data.get("reviewer_username")
        increase_reputation = serializer.data.get("increase_reputation")

        reviewer = self.__user_use_case.get_user.invoke(reviewer_username)
        if reviewer.is_admin:
            if increase_reputation:
                user_reputation = self.__score_use_case.increase_user_reputation.invoke(author_username)
            else:
                user_reputation = self.__score_use_case.decrease_user_reputation.invoke(author_username)

            return Response(
                data={
                    "userReputation": {
                        "username": user_reputation.user.username,
                        "reputation": user_reputation.reputation
                    }
                },
                status=status.HTTP_201_CREATED
            )
        else:
            if increase_reputation:
                post_reputation = self.__score_use_case.increase_post_reputation.invoke(title, author_username)
            else:
                post_reputation = self.__score_use_case.decrease_post_reputation.invoke(title, author_username)

        return Response(
            data={
                "postReputation": {
                    "postTitle": post_reputation.post.title,
                    "reputation": post_reputation.reputation
                },
            },
            status=status.HTTP_201_CREATED
        )