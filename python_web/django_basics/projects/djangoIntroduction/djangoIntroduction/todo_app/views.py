from django.shortcuts import render
from django.http import HttpResponse

from djangoIntroduction.todo_app.models import Task


# def first_view(request):
#     return HttpResponse("<h1>Hello!</h1>")  # MIME TYPE text/html (can return any MIME TYPE)
#
#
# def add_view(request):
#     return HttpResponse("<h1>Add View</h1>")
#
#
# def delete_view(request):
#     return HttpResponse("<h1>Delete View</h1>")


def index(request):
    # tasks = Task.objects.all()

    title_filter = request.GET.get("title_filter", "")

    tasks = Task.objects.filter(name__icontains = title_filter)

    context = {
        "title_filter": title_filter,
        "tasks": tasks,
    }

    return render(request, "tasks/index.html", context)