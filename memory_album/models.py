from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class UserGallery(models.Model):
    photographer = models.ForeignKey(User,
                                     on_delete=models.CASCADE)
    title = models.CharField(max_length=250, unique=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='gallery')
    
    
    def get_absolute_url(self):
        return reverse('memory_album:memory_album', kwargs={'id': self.id})
    
    def __str__(self):
        return self.photographer.first_name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)