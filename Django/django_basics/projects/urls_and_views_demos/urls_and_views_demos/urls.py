"""
URL configuration for urls_and_views_demos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from urls_and_views_demos.departments.views import index

urlpatterns = (
    path("admin/", admin.site.urls),

    # path("", index), !!!!!!!!!!

    path("", include("urls_and_views_demos.core.urls")),
    # `str` type is after `int`, last is `REGEX`
    # Prefix all urls in `urls_and_views_demos.departments.ursl` with `departments/`
    path("departments/", include("urls_and_views_demos.departments.urls")),

)

"""
When creating new Django App:
1. Add the Django app in `INSTALLED_APPS`
2. Create `urls.py` in the Django App
3. Include the Django App's `urls.py` in project/global `urls.py` even it is empty

"""
