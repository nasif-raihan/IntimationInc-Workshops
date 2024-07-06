from typing import Self

from rest_framework import serializers

from .models import User, Blog


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True, max_length=255)
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    is_active = serializers.BooleanField(default=True)
    is_staff = serializers.BooleanField(default=False)
    is_admin = serializers.BooleanField(default=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "password",
            "is_active",
            "is_staff",
            "is_admin",
            "created_at",
            "updated_at",
        ]

    @staticmethod
    def validate_email(value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    @staticmethod
    def validate_username(value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                "A user with this username already exists."
            )
        return value

    def create(self, validated_data: dict) -> User:
        user = User(
            email=validated_data["email"],
            username=validated_data["username"],
        )
        user.set_password(validated_data["password"])
        user.is_active = validated_data.get("is_active", True)
        user.is_staff = validated_data.get("is_staff", False)
        user.is_admin = validated_data.get("is_admin", False)
        user.save()
        return user

    def update(self, instance: Self, validated_data: dict) -> Self:
        instance.email = validated_data.get("email", instance.email)
        instance.username = validated_data.get("username", instance.username)
        if "password" in validated_data:
            instance.set_password(validated_data["password"])
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.is_staff = validated_data.get("is_staff", instance.is_staff)
        instance.is_admin = validated_data.get("is_admin", instance.is_admin)
        instance.save()
        return instance


class BlogSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=200)
    content = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(read_only=True)
    last_modified = serializers.DateTimeField(read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = ["id", "title", "content", "created_at", "last_modified", "author"]

    def create(self, validated_data: dict):
        request = self.context.get("request", None)
        if request and hasattr(request, "user"):
            validated_data["author"] = request.user
        return super().create(validated_data)

    def update(self, instance: Self, validated_data: dict) -> Self:
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.save()
        return instance
