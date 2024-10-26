from django.core.validators import MinLengthValidator
from django.db import models

from FruitipediaApp.fruits.validators import OnlyLettersValidator


class Fruit(models.Model):
    NAME_MAX_LENGTH = 30
    NAME_MIN_LENGTH = 2

    fruit_name = models.CharField(
        max_length = NAME_MAX_LENGTH,
        validators = [
            MinLengthValidator(NAME_MIN_LENGTH),
            OnlyLettersValidator()
        ],
        unique = True,
    )

    fruit_image_url = models.URLField()

    fruit_description = models.TextField()

    nutrition_info = models.TextField(
        blank = True,
        null = True,
    )

    owner = models.ForeignKey(
        to = "profiles.Profile",
        on_delete = models.CASCADE,
        related_name = "fruits",
    )

