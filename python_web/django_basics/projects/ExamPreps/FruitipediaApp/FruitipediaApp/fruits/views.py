from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from FruitipediaApp.fruits.forms import FruitCreateForm, FruitEditForm, FruitDeleteForm
from FruitipediaApp.fruits.models import Fruit
from FruitipediaApp.utils import get_user_obj


class FruitCreateView(CreateView):
    model = Fruit
    template_name = "fruits/create-fruit.html"
    form_class = FruitCreateForm
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class FruitDetailsView(DetailView):
    model = Fruit
    template_name = "fruits/details-fruit.html"
    pk_url_kwarg = "fruitId"


class FruitEditView(UpdateView):
    model = Fruit
    template_name = "fruits/edit-fruit.html"
    form_class = FruitEditForm
    pk_url_kwarg = "fruitId"
    success_url = reverse_lazy("dashboard")


class FruitDeleteView(DeleteView):
    model = Fruit
    template_name = "fruits/delete-fruit.html"
    form_class = FruitDeleteForm
    pk_url_kwarg = "fruitId"
    success_url = reverse_lazy("dashboard")

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)







