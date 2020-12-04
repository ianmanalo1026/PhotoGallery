
from django.urls import path
from management import views
from .views import MyProfileView

app_name = 'management'

urlpatterns = [
    path('', views.home, name='home'),
    path('signupuser/', views.signupuser, name='signupuser'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    
    path('myprofile/', MyProfileView.as_view(), name='myprofile'),
]