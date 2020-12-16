from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    MemoryGalleryListView,
    MemoryGalleryDetailView,
    MemoryGalleryCreateView, 
    MemoryGalleryUpdateView, 
    MemoryGalleryDeleteView,
    MemoryGalleryFilterListView,
    MemoryGalleryFilterOtherListView,
)

app_name = 'memory_album'

urlpatterns = [
    path('', MemoryGalleryListView.as_view(), name='memory_album'),
    path('my_gallery/', MemoryGalleryFilterListView.as_view(), name='my_gallery'),
    path('photographer/', MemoryGalleryFilterOtherListView.as_view(), name='photographer'),
    path('create/', MemoryGalleryCreateView.as_view(), name='create'),
    path('<int:pk>/', MemoryGalleryDetailView.as_view(), name='detail'),
    path('<int:pk>/delete', MemoryGalleryDeleteView.as_view(), name='delete'),
    path('<int:pk>/update', MemoryGalleryUpdateView.as_view(), name='update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)