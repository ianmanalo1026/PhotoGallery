from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from management.models import Profile


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True)
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
            'email': None,
        }
        
  
class UserEditForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        
class ProfileEditForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = [
            'introduction',
            'phone_number',
            'profile_photo',
        ]