from django.urls import path, include

from petstagram.photos import views

urlpatterns = [
    path("add/", views.photo_add, name = "photo_add"),
    path("<int:pk>/", include([
        path("", views.photo_details, name = "photo_details"),
        path("edit/", views.photo_edit, name = "photo_edit"),
    ]))
]