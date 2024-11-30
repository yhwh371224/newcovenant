from django.urls import path
from . import views

app_name = "basecamp"

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about_us, name='about_us'),
    path('home/', views.home, name='home'),    
    path('information/', views.information, name='information'),    
    path('meeting_point/', views.meeting_point, name='meeting_point'),     
    path('payment_options/', views.payment_options, name='payment_options'),    
    path('payonline/', views.payonline, name='payonline'),
    path('payonline_stripe/', views.payonline_stripe, name='payonline_stripe'),    
]


