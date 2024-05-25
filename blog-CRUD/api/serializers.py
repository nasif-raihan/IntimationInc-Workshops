from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ("id", "title", "content", "created_at", "last_modified", "created_by")

    @staticmethod
    def validate_title(value):
        if len(value) > 200 or len(value) < 5:
            raise serializers.ValidationError(
                "Title length must be in between 5 to 200"
            )
        return value

    def validate(self, data):
        # created_at and last_modified are automatically managed fields,
        # so they might not be part of the data during creation.
        # This check is only relevant if these fields are being explicitly set in the serializer.
        if "created_at" in data and "last_modified" in data:
            if data["created_at"] > data["last_modified"]:
                raise serializers.ValidationError(
                    "Update must be occurred after creation"
                )
        return data
