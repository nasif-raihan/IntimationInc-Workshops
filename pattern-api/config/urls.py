from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
]
