from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    photo_image = models.ImageField(upload_to="user_photos")

    def __str__(self):
        return f"{self.title} - youpi"
