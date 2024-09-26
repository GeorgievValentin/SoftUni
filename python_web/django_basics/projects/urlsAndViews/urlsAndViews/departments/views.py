from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from urlsAndViews.departments.models import Department


def index(request):
    return HttpResponse("<h1>Hello!</h1>")


def view_with_args_and_kwargs(request, *args, **kwargs):
    return HttpResponse(f"<h1>Args: {args}, Kwargs: {kwargs}</h1>")


def view_with_name(request, variable):  # MUST be named the same way as is the urls
    # return HttpResponse(f"<h1>Variable: {variable}</h1>")
    return render(request, "departments/name_template.html", {"variable": variable})


def view_with_pk(request, pk: int):
    # return HttpResponse(f"<h1>Integer primary key  with pk: {pk}")
    return JsonResponse({"pk": pk})  # option 2 makes same thing with abstraction


def view_with_slug(request, pk: int, slug: str):
    # # OPTION 1 FOR 404
    # # department = Department.objects.get(pk = pk, slug = slug)
    # department = Department.objects.filter(pk = pk, slug = slug)
    #
    # if not department:
    #     raise Http404("No such department")
    #
    # return HttpResponse(f"<h1>Department info from slug:<br> <h1>{department.first()}</h1>")

    # OPTION 2
    department = get_object_or_404(Department, pk = pk, slug = slug)

    return HttpResponse(f"<h1>Department info from slug:<br> <h1>{department}</h1>")


def redirect_to_softuni(request):
    return redirect("https://softuni.bg")


# OPTION 1 - Breaks the Abstraction
# def redirect_to_view(request):
#     return redirect("http://localhost:8000")

# OPTION 2
# def redirect_to_view(request):
#     return redirect(index) Breaks single responsibility if view is form an other app

# OPTION 3 - BEST OPTION


def redirect_to_view(request):
    return redirect("numbers", pk = 2)



