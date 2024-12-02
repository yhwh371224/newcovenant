from django.contrib import admin
from .models import Members, Column, Bulletin


class MembersAdmin(admin.ModelAdmin):
    list_display = ['english_name', 'korean_name', 'contact', 'email', 'suburb']
    search_fields = ['english_name', 'korean_name', 'contact', 'email', 'suburb']


class ColumnAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'updated']
    search_fields = ['title', 'author', 'created', 'updated']


class BulletinAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'created')


admin.site.register(Members, MembersAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Bulletin, BulletinAdmin)