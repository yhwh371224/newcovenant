from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Gallery, Comment


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['date', 'name', 'title', 'created']
    search_fields = ['date', 'name']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['Gallery', 'author', 'created_at', 'modified_at']
    search_fields = ['author', 'created_at', 'modified_at']


class MyAdminSite(AdminSite):
    site_header = 'NewCovenant administration'


admin.site.register(Comment, CommentAdmin)
admin.site.register(Gallery, GalleryAdmin)
