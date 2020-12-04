
from django.urls import path
from management import views

app_name = 'management'

urlpatterns = [
    path('', views.home, name='home'),
    path('signupuser/', views.signupuser, name='signupuser'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    
    path('myprofile/', views.myprofile, name='myprofile'),
    path('myprofile/updateprofile/', views.updateprofile, name='updateprofile'),
]