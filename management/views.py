from django.shortcuts import render, redirect
from management.forms import UserCreateForm, ProfileEditForm, UserEditForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
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
            address = form.cleaned_data.get('address')
            website = form.cleaned_data.get('website')
            linked_in = form.cleaned_data.get('linked_in')
            instagram = form.cleaned_data.get('instagram')
            twitter = form.cleaned_data.get('twitter')
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


@login_required
def myprofile(request):
    return render(request, 'management/myprofile.html')
    

@login_required
def updateprofile(request):
    if request.method == "POST":
        u_form = UserEditForm(request.POST, instance=request.user)
        p_form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            message = messages.success(request, f'Succesfully updated your profile')
            return redirect('management:myprofile')
    else:
        u_form = UserEditForm(instance=request.user)
        p_form = ProfileEditForm(instance=request.user.profile)
        context = {'u_form': u_form, 'p_form': p_form}
        
    return render(request, 'management/updateprofile.html', context)


