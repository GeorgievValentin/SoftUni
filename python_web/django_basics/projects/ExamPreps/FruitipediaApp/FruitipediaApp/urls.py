from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("FruitipediaApp.common.urls")),
    path("profile/", include("FruitipediaApp.profiles.urls")),
    path("fruit/", include("FruitipediaApp.fruits.urls")),
]
