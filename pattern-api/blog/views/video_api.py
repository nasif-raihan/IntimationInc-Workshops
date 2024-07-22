import json

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from di.use_case import MiscellaneousUseCase


class VideoAPI(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self):
        self.__use_case = MiscellaneousUseCase()

    def get(self, request) -> Response:
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return Response(
                data={"message": "Invalid JSON payload"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        video_id = data.get("videoId")
        if video_id is None:
            return Response(
                data={"message": "Invalid request payload"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        video = self.__use_case.get_video.invoke(video_id)

        if video is None:
            return Response(
                data={"message": "Invalid request payload"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            data={"videoId": video.video_id, "url": video.url},
            status=status.HTTP_200_OK,
        )
