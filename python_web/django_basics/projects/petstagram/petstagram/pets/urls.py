from django.urls import path, include

from petstagram.pets import views


urlpatterns = [
    path("add/", views.pet_add, name = "add"),
    path("<str:username>/pet/<slug:pet_slug>/", include([
        path("", views.pet_details, name = "pet_details"),
        path("edit/", views.pet_edit, name = "pet_edit"),
        path("delete/", views.pet_delete, name = "pet_delete"),
    ]))

]