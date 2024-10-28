from django import forms

from FurryFunniesApp.mixins import CapitalizeLabelsMixin
from FurryFunniesApp.profiles.models import Author


class AuthorBaseForm(forms.ModelForm):
    class Meta:
        fields = "__all__"


class AuthorCreateForm(CapitalizeLabelsMixin, AuthorBaseForm):
    class Meta:
        model = Author
        fields = ("first_name", "last_name", "passcode", "pets_number")
        widgets = {
            "first_name": forms.TextInput(attrs = {"placeholder": "Enter your first name..."}),
            "last_name": forms.TextInput(attrs = {"placeholder": "Enter your last name..."}),
            "passcode": forms.PasswordInput(attrs = {"placeholder": "Enter 6 digits..."}),
            "pets_number": forms.NumberInput(attrs = {"placeholder": "Enter the number of your pets..."}),
        }
        labels = {
            "passcode": "Passcode:",
        }


class AuthorEditForm(CapitalizeLabelsMixin, AuthorBaseForm):
    class Meta:
        model = Author
        exclude = ("passcode",)
