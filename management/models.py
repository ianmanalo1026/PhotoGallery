from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    profile = models.ForeignKey(User, 
                                on_delete=models.CASCADE
                                )
    introduction = models.TextField()
    phone_number = models.IntegerField()
    profile_photo = models.ImageField(upload_to=None)
    
    def __str__(self):
        return str(self.profile)
    

class UserGallery(models.Model):
    photographer = models.OneToOneField(
                                        UserProfile,
                                        on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to=None)
    
    def __str__(self):
        return self.photographer
    


