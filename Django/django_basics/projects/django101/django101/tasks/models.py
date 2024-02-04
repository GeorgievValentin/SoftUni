from django.db import models


# Create your models here.

class Task(models.Model):
    #  CharField => string (VARCHAR, varying char, ...)
    title = models.CharField(
        max_length=120,
    )

    description = models.TextField()

    done = models.BooleanField(default=False)
