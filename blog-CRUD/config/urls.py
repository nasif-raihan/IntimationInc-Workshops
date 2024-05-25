from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import BlogPostViewSet

router = DefaultRouter()
router.register(prefix="api/v1", viewset=BlogPostViewSet, basename="blog")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("rest_framework.urls", namespace="Rest_framework")),
    path("", include(router.urls)),
]
