from django.urls import path, include

from petstagram.accounts import views

urlpatterns = [
    path("login/", views.login, name = "login"),
    path("register/", views.register, name = "register"),
    path("profile/<int:pk>/", include([
        path("", views.profile_details, name = "profile_details"),
        path("edit/", views.profile_edit, name = "profile_edit"),
        path("delete/", views.profile_delete, name = "profile_delete"),
    ])),
]
