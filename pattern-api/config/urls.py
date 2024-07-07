from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog import views

router = DefaultRouter()
<<<<<<< HEAD
router.register(prefix="blog_post", viewset=views.BlogPostAPI, basename="blog_post")
=======
router.register(prefix="blog", viewset=views.BlogAPI, basename="blog")
>>>>>>> origin/main
router.register(prefix="user", viewset=views.UserAPI, basename="user")

urlpatterns = [path("admin/", admin.site.urls), path("", include(router.urls))]
