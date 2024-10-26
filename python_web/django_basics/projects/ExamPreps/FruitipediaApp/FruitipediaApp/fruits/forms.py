from django import forms
from FruitipediaApp.fruits.models import Fruit
from FruitipediaApp.mixins import PlaceholderMixin, DisableFieldsMixin  # LabelMixin, DisableFieldsMixin


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ("owner",)
        labels = {
            "fruit_name": "Name:",
            "fruit_image_url": "Image URL:",
            "fruit_description": "Description:",
            "nutrition_info": "Nutrition:",
        }
        error_messages = {
            "fruit_name": {
                "unique": "This fruit name is already in use! Try a new one.",
            },
        }


class FruitCreateForm(PlaceholderMixin, FruitBaseForm):
    pass


class FruitEditForm(FruitBaseForm):
    pass


class FruitDeleteForm(DisableFieldsMixin, FruitBaseForm):
    disabled_fields = ("__all__",)
