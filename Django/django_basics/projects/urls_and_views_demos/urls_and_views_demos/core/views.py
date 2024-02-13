from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index_no_template(request, *args, **kwargs):
    content = f"<h1>It works with:</h1><br/>" + \
              f" args = {args} and kwargs = {kwargs},<br/> " + \
              f"from path {request.path}, <br/>" + \
              f"methods = {request.method}, <br/>" + \
              f"user = {request.user}"

    return HttpResponse(
        content,
        # status=201,
        # content_type="application/json"
    )


def index(request, *args, **kwargs):
    context = {
        "title": "Request data",
        "ags": args,
        "kwargs": kwargs,
        "path": request.path,
        "method": request.method,
        "user": request.user,
    }
    return render(request, "core/index.html", context)


def redirect_to_softuni(request):
    return redirect("https://softuni.bg")


def redirect_to_index(request):
    return redirect("index_no_params")


def redirect_to_index_with_params(request):
    return redirect("index_with_pk_and_slug", pk=19, slug="Valio")


def index_json(request, *args, **kwargs):
    content = {
        "ags": args,
        "kwargs": kwargs,
        "path": request.path,
        "method": request.method,
        "user": str(request.user),
    }

    return JsonResponse(
        content,
        # status=201,
        # content_type="application/json",
    )


def raise_error(request):
    return HttpResponseNotFound()


def raise_exception(request):
    raise Http404
