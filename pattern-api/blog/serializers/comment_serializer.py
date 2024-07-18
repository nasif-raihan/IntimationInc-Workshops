from rest_framework import serializers


class CommentSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length=255)
    text = serializers.CharField()
