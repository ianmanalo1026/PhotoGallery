from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

def get_upload_path(instance, filename):
    return 'Photo_Gallery/{0}/{1}'.format(instance.photographer.username, filename)
class UserGallery(models.Model):
    photographer = models.ForeignKey(User,
                                     on_delete=models.CASCADE)
    title = models.CharField(max_length=250, unique=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    photo = models.ImageField(upload_to=get_upload_path)
    
    
    def __str__(self):
        return self.photographer
    
    def get_absolute_url(self, *args, **kwargs):
        return reverse('memory_album:detail', kwargs={'pk':self.pk})
    
    
    
    
