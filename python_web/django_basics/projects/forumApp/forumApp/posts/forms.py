from django import forms
from django.core.exceptions import ValidationError
from django.forms import formset_factory

from forumApp.posts.mixisns import DisableFieldsMixin
from forumApp.posts.models import PostModel, CommentModel


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = "__all__"

        error_messages = {
            "title": {
                "required": f"The title can't be empty! Write it!",
                "max_length": f"The title is too long! Keep it no longer than {PostModel.TITLE_MAX_LENGTH}!",
            },
            "author": {
                "required": f"The author can't be empty! Write it!",
                "max_length": f"The author's name is too long! Keep it no longer than {PostModel.AUTHOR_MAX_LENGTH}",
            },
            "content": {
                "required": "You can't create an empty post!",
            },
        }

    def clean_author(self):  # This validation is better to be set in the model... it is here only for example
        author = self.cleaned_data.get("author")

        if not author[0].isupper():
            raise ValidationError("The author's name must start with a Capital letter ")

        return author

    def clean(self):
        cleaned_data = super().clean()  # !!!!!!

        title = self.cleaned_data.get("title")
        content = self.cleaned_data.get("content")

        if title and content and title in content:
            raise ValidationError("You can't use the title in the content")

    def save(self, commit = True):
        post = super().save(commit = False)

        post.title = post.title.capitalize()

        if commit:
            post.save()

        return post

    # def clean_title(self):
    #     title = self.cleaned_data.get("title")
    #
    #     if not title[0].isupper():
    #         title = title.capitalize()
    #     return title


class PostAddForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm, DisableFieldsMixin):
    disabled_fields = ("__all__",)


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


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ("author", "content")

        labels = {
            "author": "",
            "content": "",
        }

        error_messages = {
            "author": {
                "required": "Write th author's name!",
                "max_length": f"Authors name can't be longer than {CommentModel.AUTHOR_MAX_LENGTH}"
            },
            "content": {
                "required": "Write your comment. It can't be empty!"
            },

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["author"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Your name",
        })

        self.fields["content"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Your comment"
        })


CommentFormSet = formset_factory(PostCommentForm, extra = 1)

