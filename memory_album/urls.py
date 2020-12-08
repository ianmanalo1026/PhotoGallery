from django.urls import path
from .views import MemoryGalleryCreateView, MemoryGalleryListView, MemoryGalleryDetailView

app_name = 'memory_album'

urlpatterns = [
    path('', MemoryGalleryListView.as_view(), name='memory_album'),
    path('create/', MemoryGalleryCreateView.as_view(), name='create'),
    path('<int:id>/', MemoryGalleryDetailView.as_view(), name='detail'),
]