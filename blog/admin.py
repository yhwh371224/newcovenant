from django.contrib import admin
from .models import Members, Bulletin


class MembersAdmin(admin.ModelAdmin):
    list_display = ['english_name', 'korean_name', 'contact', 'email', 'suburb']
    search_fields = ['english_name', 'korean_name', 'contact', 'email', 'suburb']


class BulletinAdmin(admin.ModelAdmin):
    list_display = ('date', 'created')


admin.site.register(Members, MembersAdmin)
admin.site.register(Bulletin, BulletinAdmin)