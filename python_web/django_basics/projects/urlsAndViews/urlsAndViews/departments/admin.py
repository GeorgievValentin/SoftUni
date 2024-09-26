from django.contrib import admin

from urlsAndViews.departments.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    ...