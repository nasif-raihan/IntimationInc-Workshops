from rest_framework.test import APITestCase, APIClient
from ..models import BlogPost
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status


class BlogPostAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testUser", email="test@mail.com", password="testPassword"
        )
        self.blog_post = BlogPost.objects.create(
            title="Initial Title", content="Initial Content", created_by=self.user
        )
        self.blog_post_data = {
            "title": "Valid Blog Post Title",
            "content": "This is a valid content for the blog post.",
            "created_by": self.user.id,
        }
        self.blog_post_url = reverse("blog-list")  # basename="blog"
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_list_blog_post(self):
        response = self.client.get(self.blog_post_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_valid_blog_post(self):
        response = self.client.post(
            self.blog_post_url, self.blog_post_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], self.blog_post_data.get("title"))
        self.assertEqual(response.data["content"], self.blog_post_data.get("content"))

    def test_create_invalid_blog_post(self):
        self.blog_post_data["title"] = "TDD"
        response = self.client.post(
            path=self.blog_post_url, data=self.blog_post_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data)
        self.assertEqual(
            response.data.get("title")[0], "Title length must be in between 5 to 200"
        )

    def test_retrieve_blog_post(self):
        url = reverse(viewname="blog-detail", kwargs={"pk": self.blog_post.pk})
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("title"), self.blog_post.title)

    def test_update_blog_post(self):
        update_data = {
            "title": "Updated Title",
            "content": "Updated content.",
            "created_by": self.user.id,
        }
        url = reverse(viewname="blog-detail", kwargs={"pk": self.blog_post.pk})
        response = self.client.put(path=url, data=update_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("title"), update_data.get("title"))
        self.assertEqual(response.data.get("content"), update_data.get("content"))

    def test_delete_blog_post(self):
        url = reverse(viewname="blog-detail", kwargs={"pk": self.blog_post.pk})
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(BlogPost.objects.filter(pk=self.blog_post.pk).exists())
