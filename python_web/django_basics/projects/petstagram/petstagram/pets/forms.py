from django import forms

from petstagram.mixins import DisableFieldsMixin
from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ["name", "date_of_birth", "personal_pet_photo"]

        widgets = {
            "name": forms.TextInput(
                attrs = {
                    "placeholder": "Pet name",
                }),
            "date_of_birth": forms.DateInput(
                attrs = {
                    "type": "date",
                }),
            "personal_pet_photo": forms.TextInput(
                attrs = {
                    "placeholder": "Link to image",
                    "label": "Personal photo"
                }),
        }

        labels = {
            "personal_pet_photo": "Personal photo",
        }


class PetAddForm(PetBaseForm):
    pass


class PetDeleteForm(PetBaseForm, DisableFieldsMixin):
    disabled_fields = ("__all__",)
    pass


class PetEditForm(PetBaseForm):
    pass

