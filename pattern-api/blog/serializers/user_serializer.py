from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.EmailField(max_length=255)
    isActive = serializers.BooleanField(default=True)
    isStaff = serializers.BooleanField(default=False)
    isAdmin = serializers.BooleanField(default=False)
