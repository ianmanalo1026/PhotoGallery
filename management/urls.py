from django.urls import path
from management import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'management'

urlpatterns = [
    path('', views.home, name='home'),
    path('signupuser/', views.signupuser, name='signupuser'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    
    path('myprofile/', views.myprofile, name='myprofile'),
    path('myprofile/updateprofile/', views.updateprofile, name='updateprofile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)