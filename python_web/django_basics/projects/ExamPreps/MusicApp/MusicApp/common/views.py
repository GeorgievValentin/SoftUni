from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from MusicApp.albums.models import Album
from MusicApp.profiles.forms import ProfileCreateForm
from MusicApp.utils import get_user_obj


class HomePageView(ListView, BaseFormView):
    model = Album
    form_class = ProfileCreateForm
    success_url = reverse_lazy("home")

    def get_template_names(self):
        profile = get_user_obj()
        if profile:
            return ["profiles/home-with-profile.html"]

        return ["profiles/home-no-profile.html"]

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)