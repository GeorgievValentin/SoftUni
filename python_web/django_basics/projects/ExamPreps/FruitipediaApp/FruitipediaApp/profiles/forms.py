from django import forms
from FruitipediaApp.mixins import PlaceholderMixin, CapitalizeLabelsMixin, DisableFieldsMixin
from FruitipediaApp.profiles.models import Profile


class ProfileBaseForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "email", "password")
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ""


class ProfileEditForm(CapitalizeLabelsMixin, ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "image_url", "age")


