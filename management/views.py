from django.shortcuts import render, redirect
from management.forms import UserCreateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import (CreateView,
                                  DetailView)
from management.models import Profile, UserGallery
from django.contrib import messages


def signupuser(request):
    """Create User"""
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            password = form.cleaned_data.get('password')
            message = messages.success(request, 
                                       f'User has been created')
            return redirect('management:signupuser')
    else:
        form = UserCreateForm()
    return render(request, 'management/signupuser.html', {'form':form})

def loginuser(request):
    """Login functionallity of the page"""
    if request.method == 'GET':
        return render(request, 
                      'management/loginuser.html',
                      {'form':AuthenticationForm()}
                      )
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password']
                            )
        if user is None:
            return render(request,
                          'management/loginuser.html',
                          {'form':AuthenticationForm(),
                           'error':'Username or Password is incorrect'}
                          )
        else:
            login(request, user)
            return redirect('management:home')
        
@login_required    
def logoutuser(request):
    """Logout functionallity of the page"""
    if request.method == "GET":
        logout(request)
        message = messages.success(request, 
                                   f'You are successfully logout!'
                                   )
        return render(request,
                      'management/logoutuser.html'
                      )
        
        
def home(request):
    """Show the Home page"""
    return render(request, 'management/home.html')



class MyProfileView(DetailView):
    model = Profile
    context_object_name = 'profile'
    
"""class ProfileCreateView(CreateView):
    model = Profile
    fields = ['user.first_name', 'user.last_name', 'user.email', 'introduction', 'phone_number', 'profile_photo']
    """