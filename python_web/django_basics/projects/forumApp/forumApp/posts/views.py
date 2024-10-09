from django.shortcuts import render, redirect
from forumApp.posts.forms import PostAddForm, PostDeleteForm, SearchForm, PostEditForm, PostCommentForm
from forumApp.posts.models import PostModel, CommentModel


def index(request):
    context = {
        "form": "",
    }

    return render(request, "common/index.html", context)


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
    comment_form = PostCommentForm(request.POST or None)
    comments = CommentModel.objects.filter(to_post = post)

    if request.method == "POST" and comment_form.is_valid():
        comment_form = comment_form.save(commit = False)
        comment_form.to_post = post
        comment_form.save()

        return redirect("details-post", pk = post.pk)

    context = {
        "post": post,
        "comment_form": comment_form,
        "comments": comments,
    }

    return render(request, "posts/details-post.html", context)


def edit_post(request, pk: int):
    post = PostModel.objects.get(pk = pk)

    if request.method == "POST":
        form = PostEditForm(request.POST, instance = post)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = PostEditForm(instance = post)

    context = {
        "form": form,
        "post": post,
    }

    return render(request, "posts/edit-post.html", context)


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

    return render(request, "posts/delete-post.html", context)
