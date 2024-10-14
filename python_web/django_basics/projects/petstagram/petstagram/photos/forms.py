from django import forms

from petstagram.mixins import ExcludeFieldsMixin, DisableFieldsMixin
from petstagram.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = "__all__"


class PhotoAddForm(PhotoBaseForm):
    pass


class PhotoDeleteForm(PhotoBaseForm, DisableFieldsMixin, ExcludeFieldsMixin):
    disabled_fields = ("__all__",)
    excluded_fields = ("photo",)


class PhotoEditForm(PhotoBaseForm, ExcludeFieldsMixin):
    excluded_fields = ("photo",)
    pass


