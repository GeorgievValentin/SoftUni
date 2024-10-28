from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from FurryFunniesApp.posts.forms import PostCreateForm, PostEditForm, PostDeleteForm
from FurryFunniesApp.posts.models import Post
from FurryFunniesApp.utils import get_user_obj


class PostCreateView(CreateView):
    model = Post
    template_name = "posts/create-post.html"
    form_class = PostCreateForm
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        form.instance.author = get_user_obj()
        return super().form_valid(form)


class PostDetailsView(DetailView):
    model = Post
    template_name = "posts/details-post.html"
    pk_url_kwarg = "post_id"


class PostEditView(UpdateView):
    model = Post
    template_name = "posts/edit-post.html"
    form_class = PostEditForm
    pk_url_kwarg = "post_id"
    success_url = reverse_lazy("dashboard")


class PostDeleteView(DeleteView):
    model = Post
    template_name = "posts/delete-post.html"
    form_class = PostDeleteForm
    pk_url_kwarg = "post_id"
    success_url = reverse_lazy("dashboard")

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)












