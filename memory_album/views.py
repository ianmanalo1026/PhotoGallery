from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import DeleteView, UpdateView
from memory_album.forms import UserGalleryForm
from management.models import Profile
from memory_album.models import UserGallery


class MemoryGalleryListView(ListView):
    queryset = UserGallery.objects.all()
    template_name = 'memory_album/memory_album.html'
    
    
class MemoryGalleryDetailView(LoginRequiredMixin, DetailView):
    model = UserGallery
    template_name = 'memory_album/memory_album_detail.html'
    
    
class MemoryGalleryCreateView(LoginRequiredMixin, CreateView):
    model = UserGallery
    form_class = UserGalleryForm
    template_name = 'memory_album/memory_album_create.html'
    
    def form_valid(self, form):
        form.instance.photographer = self.request.user
        return super().form_valid(form)
    

class MemoryGalleryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserGallery
    fields = [
        'title',
        'description',
        'photo'
    ]
    template_name = 'memory_album/memory_album_update.html'
    
    def form_valid(self, form):
        form.instance.photographer = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.photographer:
            return True
        return False
    
    
class MemoryGalleryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = UserGallery
    success_url = 'memory:album'
    template_name = 'memory_album/memory_album_delete.html'
    success_url = ' '
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.photographer:
            return True
        return False


class MemoryGalleryFilterListView(LoginRequiredMixin,  ListView):
    model = UserGallery
    template_name = 'memory_album/memory_album_filter.html'
    
    def get_queryset(self):
        queryset = super(MemoryGalleryFilterListView, self).get_queryset()
        queryset = queryset.filter(photographer=self.request.user)
        return queryset

class MemoryGalleryFilterOtherListView(LoginRequiredMixin, ListView):
    model = UserGallery
    template_name = 'memory_album/memory_album_filter_other.html'
    
    def get_queryset(self):
        queryset = super(MemoryGalleryFilterListView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
    