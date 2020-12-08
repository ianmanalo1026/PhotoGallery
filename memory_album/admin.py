from django.contrib import admin
from memory_album.models import UserGallery


class UserGalleryAdmin(admin.ModelAdmin):
    readonly_fields = ('posted_on',)
admin.site.register(UserGallery, UserGalleryAdmin)
