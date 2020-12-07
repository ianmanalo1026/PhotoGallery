from django import forms
from memory_album.models import UserGallery



class UserGalleryCreationForm(forms.ModelForm):
    
    class Meta:
        model = UserGallery
        fields = [
            'title',
            'description',
            'photo',
        ]