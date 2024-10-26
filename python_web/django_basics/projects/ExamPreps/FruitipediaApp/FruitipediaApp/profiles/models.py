from django.core.validators import MinLengthValidator
from django.db import models

from FruitipediaApp.profiles.validators import StartsWithLetterValidator


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 25
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 35
    LAST_NAME_MIN_LENGTH = 1
    EMAIL_MAX_LENGTH = 40
    PASSWORD_MAX_LENGTH = 20
    PASSWORD_MIN_LENGTH = 8

    first_name = models.CharField(
        max_length = FIRST_NAME_MAX_LENGTH,
        validators = [
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            StartsWithLetterValidator(),
        ],
    )

    last_name = models.CharField(
        max_length = LAST_NAME_MAX_LENGTH,
        validators = [
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            StartsWithLetterValidator(),
        ],
    )

    email = models.EmailField(
        max_length = EMAIL_MAX_LENGTH,
        unique = True,
    )

    password = models.CharField(
        max_length = PASSWORD_MAX_LENGTH,
        validators = [
            MinLengthValidator(PASSWORD_MIN_LENGTH),
        ],
        help_text = "*Password length requirements: 8 to 20 characters"
    )

    image_url = models.URLField(
        blank = True,
        null = True,
    )

    age = models.IntegerField(  # I think it has to be PositiveIntegerField() but in the description is missed
        blank = True,
        null = True,
        default = 18,
    )






