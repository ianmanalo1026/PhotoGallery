from django import forms
from django.forms import fields
from django.forms.models import model_to_dict
from memory_album.models import UserGallery


class UserGalleryForm(forms.ModelForm):
    
    class Meta:
        model = UserGallery
        fields = [
            'title',
            'description',
            'photo',
        ]