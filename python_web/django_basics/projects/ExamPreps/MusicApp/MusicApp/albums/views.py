from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from MusicApp.albums.forms import AlbumAddForm, AlbumEditForm, AlbumDeleteForm
from MusicApp.albums.models import Album
from MusicApp.utils import get_user_obj


class AlbumAddView(CreateView):
    model = Album
    form_class = AlbumAddForm
    template_name = "albums/album-add.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class AlbumEditView(UpdateView):
    model = Album
    form_class = AlbumEditForm
    template_name = "albums/album-edit.html"
    success_url = reverse_lazy("home")


class AlbumDeleteView(DeleteView):
    model = Album
    form_class = AlbumDeleteForm
    pk_url_kwarg = "id"
    template_name = "albums/album-delete.html"
    success_url = reverse_lazy("home")

    def get_initial(self):
        return self.object.__dict__


class AlbumDetailsView(DetailView):
    model = Album
    template_name = "albums/album-details.html"
    pk_url_kwarg = "id"
