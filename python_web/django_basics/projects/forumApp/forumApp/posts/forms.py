from django import forms
from forumApp.posts.models import PostModel


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = "__all__"
