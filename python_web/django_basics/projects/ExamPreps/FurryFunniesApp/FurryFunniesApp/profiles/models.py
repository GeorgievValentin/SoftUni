from django.core.validators import MinLengthValidator
from django.db import models

from FurryFunniesApp.profiles.validators import OnlyLettersValidator, PasscodeValidator


class Author(models.Model):
    FIRST_NAME_MAX_LENGTH = 40
    FIRST_NAME_MIN_LENGTH = 4
    LAST_NAME_MAX_LENGTH = 50
    LAST_NAME_MIN_LENGTH = 2

    first_name = models.CharField(
        max_length = FIRST_NAME_MAX_LENGTH,
        validators = [
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            OnlyLettersValidator(),
        ],
    )

    last_name = models.CharField(
        max_length = LAST_NAME_MAX_LENGTH,
        validators = [
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            OnlyLettersValidator(),
        ],
    )

    passcode = models.CharField(
        validators = [
            PasscodeValidator(),
        ],
        help_text = "Your passcode must be a combination of 6 digits"
    )

    pets_number = models.PositiveSmallIntegerField()

    info = models.TextField(
        blank = True,
        null = True,
    )

    profile_image_url = models.URLField(
        blank = True,
        null = True,
    )











