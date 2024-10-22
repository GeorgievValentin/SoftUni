from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from petstagram.common.forms import CommentForm
from petstagram.pets.forms import PetAddForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


# def pet_add(request):
#     form = PetAddForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return redirect("profile_details", pk = 1)
#
#     context = {
#         "form": form,
#     }
#
#     return render(request, "pets/pet-add-page.html", context)


class PetAddView(CreateView):
    model = Pet
    form_class = PetAddForm
    template_name = "pets/pet-add-page.html"
    success_url = reverse_lazy("profile_details", kwargs = {"pk": 1})


def pet_delete(request, username: str, pet_slug: str):
    pet = Pet.objects.get(slug = pet_slug)
    form = PetDeleteForm(instance = pet)

    if request.method == "POST":
        pet.delete()
        return redirect("profile_details", pk = 1)

    context = {
        "pet": pet,
        "form": form,
    }

    return render(request, "pets/pet-delete-page.html", context)


class PetDeleteView(DeleteView):
    model = Pet
    template_name = "pets/pet-delete-page.html"
    context_object_name = "pet"
    success_url = reverse_lazy("profile_details", kwargs = {"pk": 1})

    def get_object(self, queryset = None):
        return Pet.objects.get(slug = self.kwargs["pet_slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PetDeleteForm(initial = self.object.__dict__)

        return context

    def delete(self, request, *args, **kwargs):
        pet = self.get_object()
        pet.delete()
        return redirect(self.success_url)


# def pet_details(request, username: str, pet_slug: str):
#     pet = Pet.objects.get(slug = pet_slug)
#     all_photos = pet.photo_set.all()
#     comment_form = CommentForm()
#
#     context = {
#         "pet": pet,
#         "all_photos": all_photos,
#         "comment_form": comment_form,
#     }
#     return render(request, "pets/pet-details-page.html", context)


class PetDetailsView(DetailView):
    model = Pet
    template_name = "pets/pet-details-page.html"
    context_object_name = "pet"
    slug_url_kwarg = "pet_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_photos"] = self.object.photo_set.all()
        context["comment_form"] = CommentForm()

        return context


# def pet_edit(request, username: str, pet_slug: str):
#     pet = Pet.objects.get(slug = pet_slug)
#     form = PetEditForm(request.POST or None, instance = pet)
#
#     if request.method == "POST" and form.is_valid():
#         pet = form.save()
#         return redirect("pet_details", username, pet.slug)
#
#     conntext = {
#         "form": form,
#         "pet": pet,
#     }
#
#     return render(request, "pets/pet-edit-page.html", conntext)


class PetEditView(UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = "pets/pet-edit-page.html"
    slug_url_kwarg = "pet_slug"
    context_object_name = "pet"

    def get_success_url(self):
        return reverse_lazy(
            "pet_details",
            kwargs = {
                "username": self.kwargs["username"],
                "pet_slug": self.kwargs["pet_slug"],
            }
        )






