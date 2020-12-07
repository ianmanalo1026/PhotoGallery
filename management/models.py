from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, 
                                on_delete=models.CASCADE
                                )
    introduction = models.TextField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='images', default='images/default.jpg')
    
    def __str__(self):
        return str(self.user.first_name)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_photo.path)
    


    


