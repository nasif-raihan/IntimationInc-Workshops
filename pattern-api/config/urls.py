from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog import views

router = DefaultRouter()
router.register(prefix="blog", viewset=views.BlogAPI, basename="blog")
router.register(prefix="user", viewset=views.UserAPI, basename="user")

urlpatterns = [path("admin/", admin.site.urls), path("", include(router.urls))]
