from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("MusicApp.common.urls")),
    path("album/", include("MusicApp.albums.urls")),
    path("profile", include("MusicApp.profiles.urls")),
]
