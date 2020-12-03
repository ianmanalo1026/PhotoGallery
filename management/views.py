from django.shortcuts import render, redirect
from django.http import HttpResponse
from management.forms import UserCreateForm, UserProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def signupuser(request):
    """Create User"""
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            message = messages.success(request, 
                                       f'User has been created')
            return redirect('management:home')
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
