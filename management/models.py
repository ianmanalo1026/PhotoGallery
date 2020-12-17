from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

def get_upload_path(instance, filename):
    return 'profile_photo/{0}/{1}'.format(instance.user.username, filename)
class Profile(models.Model):
    user = models.OneToOneField(User, 
                                on_delete=models.CASCADE
                                )
    introduction = models.TextField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    mobile_number = models.IntegerField(blank=True, null=True)
    work = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    website = models.CharField(max_length=500, blank=True, null=True)
    linked_in = models.CharField(max_length=500, blank=True, null=True)
    instagram = models.CharField(max_length=500, blank=True, null=True)
    twitter = models.CharField(max_length=500, blank=True, null=True)
    profile_photo = models.ImageField(upload_to=get_upload_path, default="default.jpg")
    
    
    def __str__(self):
        return str(self.user.first_name)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_photo.path)

        if img.height > 300 or img.width > 600:
            output_size = (300, 600)
            img.thumbnail(output_size)
            img.save(self.profile_photo.path)
    


    


