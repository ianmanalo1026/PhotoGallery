from django.urls import path
from .views import (
    MemoryGalleryListView,
    MemoryGalleryDetailView,
    MemoryGalleryCreateView, 
    MemoryGalleryUpdateView, 
    MemoryGalleryDeleteView,
    MemoryGalleryFilterListView,
)

app_name = 'memory_album'

urlpatterns = [
    path('', MemoryGalleryListView.as_view(), name='memory_album'),
    path('my_gallery/', MemoryGalleryFilterListView.as_view(), name='my_gallery'),
    path('create/', MemoryGalleryCreateView.as_view(), name='create'),
    path('<int:pk>/', MemoryGalleryDetailView.as_view(), name='detail'),
    path('<int:pk>/delete', MemoryGalleryDeleteView.as_view(), name='delete'),
    path('<int:pk>/update', MemoryGalleryUpdateView.as_view(), name='update'),
]