from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("FurryFunniesApp.common.urls")),
    path("author/", include("FurryFunniesApp.profiles.urls")),
    path("posts/", include("FurryFunniesApp.posts.urls")),
]
