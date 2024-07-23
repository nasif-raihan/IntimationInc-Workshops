import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from di.use_case import ScoreFactoryUseCase
from ..serializers import ScoreSerializer


class ScoreAPI(APIView):
    def __init__(self):
        self.__score_factory_use_case = ScoreFactoryUseCase()

    def get(self, request) -> Response:
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return Response(data={"message": "Invalid JSON payload"}, status=status.HTTP_400_BAD_REQUEST)

        title = data.get("title")
        username = data.get("username")
        if not all((title, username)):
            return Response(data={"message": "Invalid request payload"}, status=status.HTTP_400_BAD_REQUEST)

        reputation = self.__score_factory_use_case.get_reputation(title, username)

        if reputation:
            return Response(data=reputation, status=status.HTTP_200_OK)
        return Response(data={"message": "Incorrect request payload"}, status=status.HTTP_400_BAD_REQUEST)

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

        reputation = self.__score_factory_use_case.update_reputation(
            title,
            author_username,
            reviewer_username,
            increase_reputation,
        )

        return Response(data=reputation, status=status.HTTP_201_CREATED)
