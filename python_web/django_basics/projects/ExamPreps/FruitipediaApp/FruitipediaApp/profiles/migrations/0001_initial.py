# Generated by Django 5.1.2 on 2024-10-26 08:14

import FruitipediaApp.profiles.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        max_length=25,
                        validators=[
                            django.core.validators.MinLengthValidator(2),
                            FruitipediaApp.profiles.validators.StartsWithLetterValidator(),
                        ],
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        max_length=35,
                        validators=[
                            django.core.validators.MinLengthValidator(1),
                            FruitipediaApp.profiles.validators.StartsWithLetterValidator(),
                        ],
                    ),
                ),
                ("email", models.EmailField(max_length=40, unique=True)),
                (
                    "password",
                    models.CharField(
                        help_text="*Password length requirements: 8 to 20 characters",
                        max_length=20,
                        validators=[django.core.validators.MinLengthValidator(8)],
                    ),
                ),
                ("image", models.URLField(blank=True, null=True)),
                ("age", models.IntegerField(blank=True, default=18, null=True)),
            ],
        ),
    ]
