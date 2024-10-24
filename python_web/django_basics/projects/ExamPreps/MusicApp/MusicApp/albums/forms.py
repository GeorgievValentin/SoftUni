from django import forms
from MusicApp.albums.models import Album
from MusicApp.mixins import ReadOnlyMixin, PlaceholderMixin


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ("owner", )


class AlbumAddForm(PlaceholderMixin, AlbumBaseForm):
    pass


class AlbumEditForm(PlaceholderMixin, AlbumBaseForm):
    pass


class AlbumDeleteForm(ReadOnlyMixin, AlbumBaseForm):
    read_only_fields = ["album_name", "artist", "genre", "price", "description"]