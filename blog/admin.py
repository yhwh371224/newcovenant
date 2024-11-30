from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Members, Column


class MembersAdmin(admin.ModelAdmin):
    list_display = ['english_name', 'korean_name', 'contact', 'email', 'suburb']
    search_fields = ['english_name', 'korean_name', 'contact', 'email', 'suburb']


class ColumnAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'updated']
    search_fields = ['title', 'author', 'created', 'updated']


class MyAdminSite(AdminSite):
    site_header = 'NewCovenant administration'

admin_site = MyAdminSite(name='horeb_yhwh')
admin_site.register(Members, MembersAdmin)
admin_site.register(Column, ColumnAdmin)

admin.site.register(Members, MembersAdmin)
admin.site.register(Column, ColumnAdmin)
