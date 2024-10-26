from django.views.generic import TemplateView, ListView
from FruitipediaApp.fruits.models import Fruit


class HomePageView(TemplateView):
    template_name = "common/index.html"


class DashboardView(ListView):
    model = Fruit
    template_name = "common/dashboard.html"





