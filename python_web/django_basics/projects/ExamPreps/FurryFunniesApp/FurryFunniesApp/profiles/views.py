from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from FurryFunniesApp.profiles.forms import AuthorCreateForm, AuthorEditForm
from FurryFunniesApp.profiles.models import Author
from FurryFunniesApp.utils import get_user_obj


class ProfileCreateView(CreateView):
    model = Author
    template_name = "profiles/create-author.html"
    form_class = AuthorCreateForm
    success_url = reverse_lazy("dashboard")


class ProfileDetailsView(DetailView):
    template_name = "profiles/details-author.html"

    def get_object(self, queryset = None):
        return get_user_obj()


class ProfileEditView(UpdateView):
    model = Author
    template_name = "profiles/edit-author.html"
    form_class = AuthorEditForm
    success_url = reverse_lazy("profile-details")

    def get_object(self, queryset = None):
        return get_user_obj()


class ProfileDeleteView(DeleteView):
    template_name = "profiles/delete-author.html"
    success_url = reverse_lazy("home")

    def get_object(self, queryset = None):
        return get_user_obj()