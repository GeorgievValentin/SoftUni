from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from FruitipediaApp.profiles.forms import ProfileCreateForm, ProfileEditForm
from FruitipediaApp.profiles.models import Profile
from FruitipediaApp.utils import get_user_obj


class CreateProfileView(CreateView):
    model = Profile
    template_name = "profiles/create-profile.html"
    form_class = ProfileCreateForm
    success_url = reverse_lazy("dashboard")


class ProfileDetailView(DetailView):
    template_name = "profiles/details-profile.html"

    def get_object(self, queryset = None):
        return get_user_obj()


class ProfileEditView(UpdateView):
    model = Profile
    template_name = "profiles/edit-profile.html"
    form_class = ProfileEditForm
    success_url = reverse_lazy("profile-details")

    def get_object(self, queryset = None):
        return get_user_obj()


class ProfileDeleteView(DeleteView):
    template_name = "profiles/delete-profile.html"
    success_url = reverse_lazy("home")

    def get_object(self, queryset = None):
        return get_user_obj()