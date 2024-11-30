import datetime

from django.db import models
from django.apps import AppConfig
from django.urls import reverse
from django.contrib.auth.models import User


class BlogAppConfig(AppConfig):
    name = 'blog'

    def ready(self):
        from . import signals


class Members(models.Model):
    english_name = models.CharField(max_length=50, blank=False)
    korean_name = models.CharField(max_length=50, blank=False)
    contact = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=False, db_index=True, verbose_name='email') 
    street = models.CharField(max_length=50, blank=True)   
    suburb = models.CharField(max_length=50, blank=True)
    birthday = models.DateField(blank=True, null=True)
    children = models.CharField(blank=True)
    position = models.CharField(blank=True)
    vehicle = models.BooleanField(default=False, blank=True)
    attendence = models.BooleanField(default=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created'] 

    def __str__(self):
        return f"{self.korean_name} ({self.english_name})"


class Column(models.Model):
    title = models.CharField(max_length=40)  
    author = models.CharField(max_length=20, default='김곤주목사')  
    content = models.TextField(blank=True)  
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True) 

    class Meta:
        ordering = ['-created'] 

    def __str__(self):
        return self.title
    

class Bulletin(models.Model):
    title = models.CharField(max_length=100, default='교회주보')  
    date = models.DateField(blank=True, null=True)  
    pdf_file = models.FileField(upload_to='bulletins/', blank=True)  
    created = models.DateTimeField(auto_now_add=True)  

    class Meta:
        ordering = ['-date']  

    def __str__(self):
        return f"{self.title} - {self.date}"


