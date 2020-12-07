from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from memory_album.models import UserGallery
from memory_album.forms import UserGalleryCreationForm
from django.contrib.auth.models import User


class MemoryGalleryListView(ListView):
    queryset = UserGallery.objects.all()
    template_name = 'memory_album/memory_album.html'
    
    
class MemoryGalleryDetailView(DetailView):
    template_name = 'memory_album/memory_album_detail.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(UserGallery, id=id_)
    
    
class MemoryGalleryCreateView(LoginRequiredMixin, CreateView):
    model = UserGallery
    form_class = UserGalleryCreationForm
    template_name = 'memory_album/memory_album_create.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(MemoryGalleryCreateView, self).form_valid(form)
