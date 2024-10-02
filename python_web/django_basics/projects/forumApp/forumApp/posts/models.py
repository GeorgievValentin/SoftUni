from django.db import models
from forumApp.posts.choices import LanguageChoice
from forumApp.posts.validators import BadLanguageValidator


class PostModel(models.Model):
    TITLE_MAX_LENGTH = 100
    AUTHOR_MAX_LENGTH = 30
    LANGUAGE_MAX_LENGTH = 20

    title = models.CharField(
        max_length = TITLE_MAX_LENGTH,
    )

    content = models.TextField(
        validators = (
            BadLanguageValidator(),
        )
    )

    author = models.CharField(
        max_length = AUTHOR_MAX_LENGTH,
    )

    published_date = models.DateTimeField(
        auto_now_add = True,
    )

    languages = models.CharField(
        max_length = LANGUAGE_MAX_LENGTH,
        choices = LanguageChoice.choices,
        default = LanguageChoice.OTHER,
    )
