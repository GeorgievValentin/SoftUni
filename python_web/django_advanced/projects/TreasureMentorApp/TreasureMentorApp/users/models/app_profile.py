from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

UserModel = get_user_model()


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 50
    LAST_NAME_MAX_LENGTH = 50

    user = models.OneToOneField(
        to = UserModel,
        on_delete = models.CASCADE,
        primary_key = True,
    )

    first_name = models.CharField(
        max_length = FIRST_NAME_MAX_LENGTH,
        blank = True,
        null = True,
    )

    last_name = models.CharField(
        max_length = LAST_NAME_MAX_LENGTH,
        blank = True,
        null = True,
    )

    profile_image = models.ImageField(
        upload_to = "profile_pics/",
        blank = True,
        null = True,
    )

    date_joined = models.DateTimeField(
        _("date joined"),
        default = timezone.now,
    )

    def __str__(self):
        return self.user.username
