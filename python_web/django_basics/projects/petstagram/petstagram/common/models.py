from django.db import models

from petstagram.photos.models import Photo


class Comment(models.Model):
    COMMENT_MAX_LENGTH = 300

    class Meta:
        indexes = [
            models.Index(fields = ["date_time_of_publication"]),  # Indexing os type of optimization for faster ordering
        ]
        ordering = ["-date_time_of_publication"]

    comment_text = models.TextField(
        max_length = COMMENT_MAX_LENGTH,
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add = True,
    )

    to_photo = models.ForeignKey(
        to = Photo,
        on_delete = models.CASCADE,
    )


class Like(models.Model):
    to_photo = models.ForeignKey(
        to = Photo,
        on_delete = models.CASCADE,
    )
