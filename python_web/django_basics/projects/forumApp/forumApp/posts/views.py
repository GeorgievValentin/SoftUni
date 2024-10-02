from django.shortcuts import render, redirect
from forumApp.posts.forms import PostBaseForm, PostAddForm, PostDeleteForm, SearchForm
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
    form = SearchForm(request.GET)
    posts = PostModel.objects.all()

    if request.method == "GET" and form.is_valid():
        query = form.cleaned_data["query"]
        posts = posts.filter(title__icontains = query)

    context = {
        "posts": posts,
        "form": form,
    }

    return render(request, "posts/dashboard.html", context)


def add_post(request):
    form = PostAddForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()

        return redirect("dashboard")

    context = {
        "form": form,
    }

    return render(request, "posts/add-post.html", context)


def details_post(request, pk: int):
    post = PostModel.objects.get(pk = pk)

    context = {
        "post": post,
    }

    return render(request, "posts/details-post.html", context)


def edit_post(request, pk: int):
    pass



def delete_post(request, pk: int):
    post = PostModel.objects.get(pk = pk)
    form = PostDeleteForm(instance = post)

    if request.method == "POST":
        post.delete()
        return redirect("dashboard")

    context = {
        "form": form,
        "post": post,
    }

    return render(request, "posts/delete-template.html", context)
