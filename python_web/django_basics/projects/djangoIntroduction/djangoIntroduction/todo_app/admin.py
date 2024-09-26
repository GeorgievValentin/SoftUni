from django.contrib import admin

from djangoIntroduction.todo_app.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ...