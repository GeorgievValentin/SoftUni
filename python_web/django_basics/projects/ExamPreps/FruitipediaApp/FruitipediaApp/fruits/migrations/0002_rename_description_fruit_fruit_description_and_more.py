# Generated by Django 5.1.2 on 2024-10-26 18:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("fruits", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="fruit",
            old_name="description",
            new_name="fruit_description",
        ),
        migrations.RenameField(
            model_name="fruit",
            old_name="image",
            new_name="fruit_image_url",
        ),
        migrations.RenameField(
            model_name="fruit",
            old_name="name",
            new_name="fruit_name",
        ),
        migrations.RenameField(
            model_name="fruit",
            old_name="nutrition",
            new_name="nutrition_info",
        ),
    ]
