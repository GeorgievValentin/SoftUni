from datetime import datetime

from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import classonlymethod
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView, DetailView

from forumApp.posts.forms import PostAddForm, PostDeleteForm, SearchForm, PostEditForm, PostCommentForm, CommentFormSet
from forumApp.posts.models import PostModel, CommentModel


class BaseView:
    @classonlymethod
    def as_view(cls):

        def view(request, *args, **kwargs):
            view_instance = cls()
            return view_instance.dispatch(request, *args, **kwargs)

        return view

    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            return self.get(request, *args, **kwargs)
        elif request.method == "POST":
            return self.post(request, *args, **kwargs)


class IndexView(TemplateView):
    template_name = "common/index.html"   # static way
    extra_context = {
        "static_time": datetime.now(),
    }  # static way

    def get_template_names(self):  # dynamic way
        if self.request.user.is_authenticated:
            return ["common/logged_index.html"]
        else:
            return ["common/index.html"]

    def get_context_data(self, **kwargs):  # dynamic way
        contex = super().get_context_data(**kwargs)

        contex["dynamic_time"] = datetime.now()

        return contex

# def index(request):
#     post_form = modelform_factory(
#         PostModel,
#         fields = "__all__"
#     )
#
#     context = {
#         "form": post_form,
#     }
#
#     return render(request, "common/index.html", context)


class DashboardView(ListView, FormView):
    template_name = "posts/dashboard.html"
    context_object_name = "posts"
    form_class = SearchForm
    model = PostModel
    success_url = reverse_lazy("dashboard")

    def get_queryset(self):
        queryset = self.model.objects.all()

        if queryset in self.request.GET:
            query = self.request.GET.get("query")
            queryset = self.queryset.filter(title__icontains = query)

        return queryset

# def dashboard(request):
#     form = SearchForm(request.GET)
#     posts = PostModel.objects.all()
#
#     if request.method == "GET" and form.is_valid():
#         query = form.cleaned_data["query"]
#         posts = posts.filter(title__icontains = query)
#
#     context = {
#         "posts": posts,
#         "form": form,
#     }
#
#     return render(request, "posts/dashboard.html", context)


class PostAddView(CreateView):
    template_name = "posts/add-post.html"
    model = PostModel
    form_class = PostAddForm
    success_url = reverse_lazy("dashboard")

# def add_post(request):
#     form = PostAddForm(request.POST or None, request.FILES or None)
#
#     if request.method == "POST" and form.is_valid():
#         form.save()
#
#         return redirect("dashboard")
#
#     context = {
#         "form": form,
#     }
#
#     return render(request, "posts/add-post.html", context)


class PostDetailsView(DetailView):
    model = PostModel
    context_object_name = "post"
    template_name = "posts/details-post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formset"] = CommentFormSet()
        context["comments"] = self.object.comments.all()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        formset = CommentFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit = False)
                    comment.to_post = post
                    comment.save()

            return redirect("details-post", pk = post.id)

        context = self.get_context_data()
        context["formset"] = formset

        return self.render_to_response(context)


# def details_post(request, pk: int):
#     post = PostModel.objects.get(pk = pk)
#     comment_form = PostCommentForm(request.POST or None)
#     comments = CommentModel.objects.filter(to_post = post)
#
#     if request.method == "POST" and comment_form.is_valid():
#         comment_form = comment_form.save(commit = False)
#         comment_form.to_post = post
#         comment_form.save()
#
#         return redirect("details-post", pk = post.pk)
#
#     context = {
#         "post": post,
#         "comment_form": comment_form,
#         "comments": comments,
#     }
#
#     return render(request, "posts/details-post.html", context)


class PostEditView(UpdateView):
    template_name = "posts/edit-post.html"
    model = PostModel
    success_url = reverse_lazy("dashboard")
    context_object_name = "post"

    def get_form_class(self):
        if self.request.user.is_superuser:
            return modelform_factory(PostModel, fields = "__all__")
        else:
            return modelform_factory(PostModel, fields = ("content",))

# def edit_post(request, pk: int):
#     post = PostModel.objects.get(pk = pk)
#
#     if request.method == "POST":
#         form = PostEditForm(request.POST, instance = post)
#         if form.is_valid():
#             form.save()
#             return redirect("dashboard")
#     else:
#         form = PostEditForm(instance = post)
#
#     context = {
#         "form": form,
#         "post": post,
#     }
#
#     return render(request, "posts/edit-post.html", context)


class PostDeleteView(DeleteView, FormView):
    template_name = "posts/delete-post.html"
    model = PostModel
    form_class = PostDeleteForm
    success_url = reverse_lazy("dashboard")
    context_object_name = "post"

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post = PostModel.objects.get(pk = pk)
        return post.__dict__

# def delete_post(request, pk: int):
#     post = PostModel.objects.get(pk = pk)
#     form = PostDeleteForm(instance = post)
#
#     if request.method == "POST":
#         post.delete()
#         return redirect("dashboard")
#
#     context = {
#         "form": form,
#         "post": post,
#     }
#
#     return render(request, "posts/delete-post.html", context)