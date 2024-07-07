from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from di import UseCase
from ..models import User
from ..serializers import UserSerializer


class UserAPI(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._use_cases = UseCase()

    def get(self, request) -> Response:
        username = request.data.get("username")
        if not username:
            return Response(
                data={"message": "Username not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = self._use_cases.get_user.invoke(username)

        return Response(
            data={
                "email": user.email,
                "username": user.username,
                "isActive": user.is_active,
                "isStaff": user.is_staff,
                "isAdmin": user.is_admin,
                "createdAt": user.created_at,
                "updatedAt": user.updated_at,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request) -> Response:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            username = serializer.data.get("username")
            is_active = serializer.data.get("is_active")
            is_staff = serializer.data.get("is_staff")
            is_admin = serializer.data.get("is_admin")
            created_at = serializer.data.get("created_at")
            updated_at = serializer.data.get("updated_at")
            user = self._use_cases.add_user.invoke(
                user=User(
                    email=email,
                    username=username,
                    is_active=is_active,
                    is_staff=is_staff,
                    is_admin=is_admin,
                    created_at=created_at,
                    updated_at=updated_at,
                )
            )
            return Response(
                data={
                    "email": user.email,
                    "username": user.username,
                    "isActive": user.is_active,
                    "isStaff": user.is_staff,
                    "isAdmin": user.is_admin,
                    "createdAt": user.created_at,
                    "updatedAt": user.updated_at,
                },
                status=status.HTTP_201_CREATED,
            )

    def put(self, request) -> Response:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            username = serializer.data.get("username")
            is_active = serializer.data.get("is_active")
            is_staff = serializer.data.get("is_staff")
            is_admin = serializer.data.get("is_admin")
            created_at = serializer.data.get("created_at")
            updated_at = serializer.data.get("updated_at")
            user = self._use_cases.update_user.invoke(
                user=User(
                    email=email,
                    username=username,
                    is_active=is_active,
                    is_staff=is_staff,
                    is_admin=is_admin,
                    created_at=created_at,
                    updated_at=updated_at,
                )
            )
            return Response(
                data={
                    "email": user.email,
                    "username": user.username,
                    "isActive": user.is_active,
                    "isStaff": user.is_staff,
                    "isAdmin": user.is_admin,
                    "createdAt": user.created_at,
                    "updatedAt": user.updated_at,
                },
                status=status.HTTP_200_OK,
            )

    def delete(self, request) -> Response:
        username = request.data.get("username")
        if not username:
            return Response(
                data={"message": "Username not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            data={"success": self._use_cases.delete_user.invoke(username)},
            status=status.HTTP_200_OK,
        )

    @staticmethod
    def formatter(data: dict) -> dict:
        return {
            "email": data.get("email"),
            "username": data.get("username"),
            "is_active": data.get("isActive"),
            "is_staff": data.get("isStaff"),
            "is_admin": data.get("isAdmin"),
            "created_at": data.get("createdAt"),
            "updated_at": data.get("updatedAt"),
        }
