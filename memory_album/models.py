from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

def get_upload_path(instance, filename):
    return 'Photo_Gallery/{0}/{1}'.format(instance.photographer.username, filename)
class UserGallery(models.Model):
    photographer = models.ForeignKey(User,
                                     on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    posted_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    photo = models.ImageField(upload_to=get_upload_path)
    
    
    def __str__(self):
        return str(self.photographer)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)
    
    def get_absolute_url(self, *args, **kwargs):
        return reverse('memory_album:detail', kwargs={'pk':self.pk})
    
    
    
    
