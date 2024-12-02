from django.urls import path
from . import views

app_name = "basecamp"

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about_us, name='about_us'),
    path('home/', views.home, name='home'),    
    path('information/', views.information, name='information'), 
    path('introduction/', views.introduction, name='introduction'),
    path('church_bulletin/', views.church_bulletin, name='church_bulletin'),  
    path('meetings/', views.meetings, name='meetings'),  
    path('meeting_point/', views.meeting_point, name='meeting_point'),     
    path('payment_options/', views.payment_options, name='payment_options'),    
    path('payonline/', views.payonline, name='payonline'),
    path('payonline_stripe/', views.payonline_stripe, name='payonline_stripe'),    
    path('workers/', views.workers, name='workers'), 
]


