from django.urls import path
from . import views

app_name = "basecamp"

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),    
    path('introduction/', views.introduction, name='introduction'),
    path('bulletin_list/', views.bulletin_list, name='bulletin_list'),  
    path('meetings/', views.meetings, name='meetings'),   
    path('workers/', views.workers, name='workers'), 
    path('column/', views.column, name='column'),
    path('location/', views.location, name='location'),
    path('contact_list/', views.contact_list, name='contact_list'),
    path('worship_music/', views.worship_music, name='worship_music'),
]


