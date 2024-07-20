from rest_framework import serializer


class ReviewerSerializer(serializer.Serializer):
    blog_post_title = serializer.CharField(max_length=200)
    author_username = serializer.CharField(max_length=255)
    reviewer_username = serializer.CharField(max_length=255)
