from django.shortcuts import render, redirect
from forumApp.posts.forms import PostBaseForm
from forumApp.posts.models import PostModel


def index(request):
    context = {
        "form": "",
    }

    return render(request, "base.html", context)
    # context = {
    #     "current_time": datetime.now(),
    # }
    #
    # return render(request, "base.html", context)


def dashboard(request):
    context = {
        "posts": PostModel.objects.all(),
    }

    return render(request, "posts/dashboard.html", context)


def add_post(request):
    form = PostBaseForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()

        return redirect("dashboard")

    context = {
        "form": form,
    }

    return render(request, "posts/add-post.html", context)
