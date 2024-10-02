from django import forms
from forumApp.posts.models import PostModel


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = "__all__"


class PostAddForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PostDeleteForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True


class SearchForm(forms.Form):
    query = forms.CharField(
        label = "",
        required = False,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Search for a post..."
            }
        )
    )


