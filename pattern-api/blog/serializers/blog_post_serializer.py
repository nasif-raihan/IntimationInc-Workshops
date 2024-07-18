from rest_framework import serializers


class BlogPostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    content = serializers.CharField()
    username = serializers.CharField(max_length=255)
