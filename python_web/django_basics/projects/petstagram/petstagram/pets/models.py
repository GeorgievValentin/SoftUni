from django.db import models
from django.template.defaultfilters import slugify


class Pet(models.Model):
    name = models.CharField(
        max_length = 30,
    )

    personal_photo = models.URLField()

    date_of_birth = models.DateField(
        blank = True,
        null = True,
    )

    slug = models.SlugField(
        unique = True,
        null = False,
        blank = True,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")

        super().save(*args, **kwargs)
