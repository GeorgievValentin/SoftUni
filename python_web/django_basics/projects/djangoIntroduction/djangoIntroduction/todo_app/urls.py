from django.urls import path
from djangoIntroduction.todo_app.views import  index # first_view, add_view, delete_view

urlpatterns = [
    # path("", first_view),
    # path("add/", add_view),
    # path("delete/", delete_view)
    path("", index),
]