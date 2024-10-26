from django.urls import path
from django.urls import include

from FruitipediaApp.fruits import views

urlpatterns = [
    path("create/", views.FruitCreateView.as_view(), name = "fruit-create"),
    path("<int:fruitId>/", include([
        path("details/", views.FruitDetailsView.as_view(), name = "fruit-details"),
        path("edit/", views.FruitEditView.as_view(), name = "fruit-edit"),
        path("delete/", views.FruitDeleteView.as_view(), name = "fruit-delete"),
    ])),
]
