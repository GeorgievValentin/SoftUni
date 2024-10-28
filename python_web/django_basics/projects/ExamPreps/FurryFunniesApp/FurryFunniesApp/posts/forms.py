from django import forms
from FurryFunniesApp.mixins import CapitalizeLabelsMixin, ReadOnlyFieldsMixin
from FurryFunniesApp.posts.models import Post


class PostBaseForm(CapitalizeLabelsMixin, forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


class PostCreateForm(PostBaseForm):
    class Meta:
        model = Post
        exclude = ("updated_at", "author")
        widgets = {
            "title": forms.TextInput(attrs = {"placeholder": "Put an attractive and unique title..."}),
            "content": forms.Textarea(attrs = {"placeholder": "Share some interesting facts about your adorable pets..."}),
        }


class PostEditForm(PostBaseForm):
    class Meta:
        model = Post
        exclude = ("updated_at", "author")
        help_texts = {
            "post_image_url": "",
        }


class PostDeleteForm(ReadOnlyFieldsMixin, PostEditForm):
    disabled_fields = ("__all__",)
