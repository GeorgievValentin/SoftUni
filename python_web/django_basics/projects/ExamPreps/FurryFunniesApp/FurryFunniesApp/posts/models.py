from django.core.validators import MinLengthValidator
from django.db import models


class Post(models.Model):
    TITLE_MAX_LENGTH = 50
    TITLE_MIN_LENGTH = 5

    title = models.CharField(
        max_length = TITLE_MAX_LENGTH,
        validators = [
            MinLengthValidator(TITLE_MIN_LENGTH),
        ],
        unique = True,
        error_messages = {
            "unique": "Oops! That title is already taken. How about something fresh and fun?",
        },
    )

    post_image_url = models.URLField(
        help_text = "Share your funniest furry photo URL!"
    )

    content = models.TextField()

    updated_at = models.DateTimeField(
        auto_now = True,
    )

    author = models.ForeignKey(
        to = "profiles.Author",
        on_delete = models.CASCADE,
        related_name = "posts",
    )











