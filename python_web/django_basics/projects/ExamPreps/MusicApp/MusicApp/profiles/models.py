from django.core.validators import MinLengthValidator
from django.db import models
from MusicApp.profiles.validators import AlphaNumericValidator


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 15
    USERNAME_MIN_LENGTH = 2

    username = models.CharField(
        max_length = USERNAME_MAX_LENGTH,
        validators = [
            MinLengthValidator(USERNAME_MIN_LENGTH),
            AlphaNumericValidator(),
        ],
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        blank = True,
        null = True,
    )
