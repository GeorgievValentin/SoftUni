from django.shortcuts import render
from petstagram.photos.models import Photo


def photo_add(request):
    return render(request, "photos/photo-add-page.html")


def photo_details(request, pk: int):
    photo = Photo.objects.get(pk = pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()

    context = {
        "photo": photo,
        "likes": likes,
        "comments": comments,
    }

    return render(request, "photos/photo-details-page.html", context)


def photo_edit(request, pk: int):
    return render(request, "photos/photo-edit-page.html")
