from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, 
                                on_delete=models.CASCADE
                                )
    introduction = models.TextField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to=None)
    
    def __str__(self):
        return str(self.user.username)
    

class UserGallery(models.Model):
    photographer = models.OneToOneField(
                                        'Profile',
                                        on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to=None)
    
    def __str__(self):
        return self.photographer
    


