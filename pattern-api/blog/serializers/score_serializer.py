from rest_framework import serializers


class ScoreSerializer(serializers.Serializer):
    blog_post_title = serializers.CharField(max_length=200)
    author_username = serializers.CharField(max_length=255, required=True)
    reviewer_username = serializers.CharField(max_length=255, required=True)
    increase_reputation = serializers.BooleanField(default=True)
