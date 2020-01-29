from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView

from photos.models import Photo


def photo_index(request):
    photos = Photo.objects.all()
    return render(request, "photos/list_photos.html", {"photo_list": photos})

# def detail(request, photo_id):
#     return HttpResponse("You're looking at question %s." % photo_id)

def detail(request, photo_id):
    photo_detail = Photo.objects.get(id=photo_id)
    return render(request, "photos/detail.html", {"photo_detail": photo_detail})


class PhotoCreateView(CreateView):
    model = Photo
    fields = ["title", "photo_image", "description", "user"]
    template_name = "photos/photo_form.html"

    def get_success_url(self):
        return reverse("index")
