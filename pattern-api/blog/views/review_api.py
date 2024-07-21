import json

from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from di.use_case import ReviewUseCase, PostUseCase, UserUseCase
from domain.model import Review
from ..serializers import ReviewSerializer


class ReviewAPI(APIView):
    permission_classes = [IsAdminUser]

    def __init__(self):
        self.__post_use_cases = PostUseCase()
        self.__user_use_cases = UserUseCase()
        self.__review_use_case = ReviewUseCase()

    def get(self, request) -> Response:
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return Response(data={"message": "Invalid JSON payload"}, status=status.HTTP_400_BAD_REQUEST)

        review_id = data.get("review_id")
        post_title = data.get("post_title")
        author_username = data.get("author_username")
        if not all((review_id, post_title, author_username)):
            return Response(data={"message": "Invalid request payload"}, status=status.HTTP_400_BAD_REQUEST)

        review = self.__review_use_case.get_review.invoke(post_title, author_username, review_id)
        if review:
            return Response(
                data={
                    "reviewId": review.review_id,
                    "title": review.title,
                    "rating": review.rating,
                    "content": review.content,
                    "pros": review.pros,
                    "cons": review.cons,
                    "idea": review.idea,
                    "recommendation": review.recommendation,
                    "authorFeedback": review.author_feedback,
                    "postTitle": review.post.title,
                    "reviewerUsername": review.reviewer.username,
                },
                status=status.HTTP_200_OK
            )
        return Response(data={"message": "Incorrect request payload"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request) -> Response:
        serializer = ReviewSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                data={"message": "Invalid request payload"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        review_title = serializer.data.get("review_title")
        post_title = serializer.data.get("post_title")
        author_username = serializer.data.get("author_username")
        reviewer_username = serializer.data.get("reviewer_username")
        rating = serializer.data.get("rating")
        content = serializer.data.get("content")
        pros = serializer.data.get("pros")
        cons = serializer.data.get("cons")
        idea = serializer.data.get("idea")
        recommendation = serializer.data.get("recommendation")
        author_feedback = serializer.data.get("author_feedback")

        reviewer = self.__user_use_cases.get_user.invoke(reviewer_username)
        blog_post = self.__post_use_cases.get_blog_post.invoke(post_title, author_username)
        if not all((reviewer, blog_post)):
            return Response(data={"message": "Invalid request payload"}, status=status.HTTP_400_BAD_REQUEST)

        review = self.__review_use_case.add_review.invoke(
            review=Review(
                review_title,
                rating,
                content,
                pros,
                cons,
                idea,
                recommendation,
                author_feedback,
                blog_post,
                reviewer
            )
        )
        return Response(
            data={
                "review_title": review_title,
                "blog_post": {
                    "title": blog_post.title,
                    "author": blog_post.author.username,
                },
                "reviewer": reviewer.username,
                "rating": rating,
                "content": content,
                "pros": pros,
                "cons": cons,
                "idea": idea,
                "recommendation": recommendation,
                "author_feedback": author_feedback,
            },
            status=status.HTTP_201_created
        )

    def put(self, request) -> Response:
        serializer = ReviewSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                data={"message": "Invalid request payload"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        review_title = serializer.data.get("review_title")
        post_title = serializer.data.get("post_title")
        author_username = serializer.data.get("author_username")
        reviewer_username = serializer.data.get("reviewer_username")
        rating = serializer.data.get("rating")
        content = serializer.data.get("content")
        pros = serializer.data.get("pros")
        cons = serializer.data.get("cons")
        idea = serializer.data.get("idea")
        recommendation = serializer.data.get("recommendation")
        author_feedback = serializer.data.get("author_feedback")

        reviewer = self.__user_use_cases.get_user.invoke(reviewer_username)
        blog_post = self.__post_use_cases.get_blog_post.invoke(post_title, author_username)
        if not all((reviewer, blog_post)):
            return Response(data={"message": "Invalid request payload"}, status=status.HTTP_400_BAD_REQUEST)

        review = self.__review_use_case.update_review.invoke(
            review=Review(
                review_title,
                rating,
                content,
                pros,
                cons,
                idea,
                recommendation,
                author_feedback,
                blog_post,
                reviewer
            )
        )
        return Response(
            data={
                "review_title": review_title,
                "blog_post": {
                    "title": blog_post.title,
                    "author": blog_post.author.username,
                },
                "reviewer": reviewer.username,
                "rating": rating,
                "content": content,
                "pros": pros,
                "cons": cons,
                "idea": idea,
                "recommendation": recommendation,
                "author_feedback": author_feedback,
            },
            status=status.HTTP_200_OK
        )

    def delete(self, request) -> Response:
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return Response(data={"message": "Invalid JSON payload"}, status=status.HTTP_400_BAD_REQUEST)

        review_id = data.get("review_id")
        post_title = data.get("post_title")
        author_username = data.get("author_username")
        if not all((review_id, post_title, author_username)):
            return Response(data={"message": "Invalid request payload"}, status=status.HTTP_400_BAD_REQUEST)

        success = self.__review_use_case.delete_review.invoke(post_title, author_username, review_id)
        if success:
            message = "Successfully deleted the review!"
        else:
            message = "No review found against the provided info."

        return Response(
            data={"success": success, "message": message}, status=status.HTTP_200_OK
        )
