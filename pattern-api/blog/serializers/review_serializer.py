from rest_framework import serializers


class ReviewSerializer(serializers.Serializer):
    review_title = serializers.Charfield(max_length=255, required=True)
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, max_value=5, min_value=0, required=True)
    content = serializers.Charfield(allow_blank=True)
    pros = serializers.Charfield(allow_blank=True)
    cons = serializers.Charfield(allow_blank=True)
    idea = serializers.Charfield(allow_blank=True)
    recommendation = serializers.Charfield(allow_blank=True)
    author_feedback = serializers.Charfield(allow_blank=True)
    post_title = serializers.Charfield(max_length=255, required=True)
    reviewer_username = serializers.Charfield(max_length=255, required=True)
