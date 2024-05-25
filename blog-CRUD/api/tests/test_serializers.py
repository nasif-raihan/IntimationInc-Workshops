from django.contrib.auth.models import User
from django.test import TestCase
from api.models import BlogPost
from api.serializers import BlogPostSerializer


class BlogPostSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testUser", email="test@mail.com", password="testPassword"
        )
        self.blog_post_data = {
            "title": "Test Title",
            "content": "TDD reduce future maintenance cost",
            "created_by": self.user.id,
        }
        self.blog_post = BlogPost.objects.create(
            title="Initial Title", content="Initial Content", created_by=self.user
        )

    def test_valid_blog_post_serializer(self):
        serializer = BlogPostSerializer(data=self.blog_post_data)
        self.assertTrue(serializer.is_valid())
        # fmt: off
        self.assertEqual(serializer.validated_data["title"], self.blog_post_data.get("title"))
        self.assertEqual(serializer.validated_data["content"], self.blog_post_data.get("content"))
        self.assertEqual(serializer.validated_data["created_by"], self.user)
        # fmt: on

    def test_invalid_blog_post_serializer_short_title(self):
        self.blog_post_data["title"] = "TDD"
        serializer = BlogPostSerializer(data=self.blog_post_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn(member="title", container=serializer.errors)
        # fmt: off
        self.assertEqual(first=serializer.errors["title"][0], second="Title length must be in between 5 to 200")
        # fmt: on

    def test_invalid_blog_post_serializer_long_title(self):
        self.blog_post_data["title"] = "T" * 201
        serializer = BlogPostSerializer(data=self.blog_post_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("title", serializer.errors)
        # fmt: off
        self.assertEqual(serializer.errors["title"][0], "Ensure this field has no more than 200 characters.")
        # fmt: on

    #
    def test_valid_update_blog_post(self):
        update_data = {
            "title": "Updated Title",
            "content": "Updated Content",
            "created_by": self.user.id,
        }
        serializer = BlogPostSerializer(instance=self.blog_post, data=update_data)
        self.assertTrue(serializer.is_valid())
        updated_blog_post = serializer.save()
        self.assertEqual(updated_blog_post.title, update_data.get("title"))
        self.assertEqual(updated_blog_post.content, update_data.get("content"))
