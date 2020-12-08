from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from management.models import Profile

class UserGallery(models.Model):
    photographer = models.OneToOneField(User,
                                     on_delete=models.CASCADE)
    title = models.CharField(max_length=250, unique=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='gallery')
    
    def __str__(self):
        return str(self.photographer)
    