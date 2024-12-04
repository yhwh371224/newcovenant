from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Gallery, Comment


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'author' ]
    search_fields = ['title', ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author']
    search_fields = ['author']


class MyAdminSite(AdminSite):
    site_header = 'NewCovenant administration'


admin.site.register(Comment, CommentAdmin)
admin.site.register(Gallery, GalleryAdmin)
