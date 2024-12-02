from django.urls import path
from . import views

app_name = "basecamp"

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about_us, name='about_us'),
    path('home/', views.home, name='home'),    
    path('information/', views.information, name='information'), 
    path('introduction/', views.introduction, name='introduction'),
    path('bulletin_list/', views.bulletin_list, name='bulletin_list'),  
    path('meetings/', views.meetings, name='meetings'),  
    path('meeting_point/', views.meeting_point, name='meeting_point'),     
    path('payment_options/', views.payment_options, name='payment_options'),    
    path('payonline/', views.payonline, name='payonline'),
    path('payonline_stripe/', views.payonline_stripe, name='payonline_stripe'),    
    path('workers/', views.workers, name='workers'), 
    path('column/', views.column, name='column'),
    path('gallery/', views.gallery, name='gallery'),
    path('location/', views.location, name='location'),
    path('pickup/', views.pickup, name='pickup'),
    path('worship_music/', views.worship_music, name='worship_music'),

]


