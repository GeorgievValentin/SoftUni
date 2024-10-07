from django import forms
from forumApp.posts.models import PostModel


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = "__all__"

        error_messages = {
            "title": {
                "max_length": f"The title is too long! Keep it no longer than {PostModel.TITLE_MAX_LENGTH}!"
            },
            "author": {
                "max_length": f"The author's name is too long! Keep it no longer than {PostModel.AUTHOR_MAX_LENGTH}"
            },
        }


class PostAddForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


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


