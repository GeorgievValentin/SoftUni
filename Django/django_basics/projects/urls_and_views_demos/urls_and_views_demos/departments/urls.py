from django.urls import path

from urls_and_views_demos.departments.views import department_details_by_id, department_details_by_name

urlpatterns = (
    # path("departments/1/", department_1_details),
    # path("departments/2/", department_2_details),

    path("<int:pk>/", department_details_by_id),  # ->departments/<int:pk>/
    path("<str:name>/", department_details_by_name),
    # Always `int` type is first, after that `str`, `REGEX` last
)
