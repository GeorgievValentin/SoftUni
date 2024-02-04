"""
Do always when creating new Django App

1. Move to project directory
2. Create `urls.py` file
3. Register this Django app's `urls.py` file in the project's `urls.py` file
4. Register this Django App in `settings.py` -> `INSTALLED_APPS`

"""

from django.urls import path

from .views import index

urlpatterns = (
    path("", index),
)