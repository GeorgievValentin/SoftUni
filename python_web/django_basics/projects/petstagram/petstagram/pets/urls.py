from django.urls import path, include

from petstagram.pets import views
from petstagram.pets.views import PetAddView, PetEditView, PetDetailsView, PetDeleteView

urlpatterns = [
    path("add/", PetAddView.as_view(), name = "pet_add"),
    path("<str:username>/pet/<slug:pet_slug>/", include([
        path("", PetDetailsView.as_view(), name = "pet_details"),
        path("edit/",PetEditView.as_view(), name = "pet_edit"),
        path("delete/", PetDeleteView.as_view(), name = "pet_delete"),
    ])),
]