from django.urls import path, include
from urlsAndViews.departments import views

urlpatterns = [
    path("", views.index, name = "home"),
    path("redirect-to-view/", views.redirect_to_view, name = "redirect_to_view"),
    path("softuni/", views.redirect_to_softuni),
    path("numbers/", include([
        path("<int:pk>/", views.view_with_pk, name = "numbers"),
        path("<int:pk>/<slug:slug>/", views.view_with_slug),
    ])),
    # path("<variable>/", views.view_with_name),
    path("args-and-kwargs/<param>/", views.view_with_args_and_kwargs),  # matches till `/`
    path("<path:variable>/", views.view_with_name),  # matches after the `/` as well
]
