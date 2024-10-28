from django.views.generic import TemplateView, ListView
from FurryFunniesApp.posts.models import Post


class HomePageView(TemplateView):
    template_name = "common/index.html"


class DashboardView(ListView):
    model = Post
    template_name = "common/dashboard.html"

