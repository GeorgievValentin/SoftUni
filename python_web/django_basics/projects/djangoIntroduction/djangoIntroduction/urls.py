"""
STEP 1: Create a project
Step 2: Create an app
Step 3: Add the app to `INSTALLED_APPS`
Step 4: Replace DB settings with Postgres settings
Step 5: Enter credentials
Step 6: Install psycopg2
Step 7: Create the database

"""


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("djangoIntroduction.todo_app.urls"))
]
