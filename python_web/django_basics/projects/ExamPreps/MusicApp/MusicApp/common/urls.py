from django.urls import path

from MusicApp.common import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),

]