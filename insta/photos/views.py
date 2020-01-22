from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView

from photos.models import Photo


def photo_index(request):
    photos = Photo.objects.all()
    return render(request, "photos/list_photos.html", {"photo_list": photos})


class PhotoCreateView(CreateView):
    model = Photo
    fields = ["title", "photo_image", "description", "user"]
    template_name = "photos/photo_form.html"

