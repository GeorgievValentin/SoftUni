from django.urls import path, include

from forumApp.posts import views
from forumApp.posts.views import IndexView, PostAddView, DashboardView, PostEditView, PostDeleteView, PostDetailsView

urlpatterns = [
    path("", IndexView.as_view(), name = "index"),
    path("dashboard/", DashboardView.as_view(), name = "dashboard"),
    path("add-post/", PostAddView.as_view(), name = "add-post"),
    path("<int:pk>/", include([
        path("edit-post/", PostEditView.as_view(), name = "edit-post"),
        path("details-post/", PostDetailsView.as_view(), name = "details-post"),
        path("delete-post/", PostDeleteView.as_view(), name = "delete-post"),
    ])),
]
