import datetime

from django.db import models
from django.apps import AppConfig
from django.urls import reverse
from django.contrib.auth.models import User


class BlogAppConfig(AppConfig):
    name = 'blog'

    def ready(self):
        from . import signals


class Post(models.Model):
    name = models.CharField(max_length=100, blank=False)
    contact = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(blank=False, db_index=True, verbose_name='email') 
    street = models.CharField(max_length=200, blank=True, null=True)   
    suburb = models.CharField(max_length=100, blank=True, null=True)
    birthday = models.TextField(blank=True, null=True)
    children = models.TextField(blank=True, null=True)
    position = models.TextField(blank=True, null=True)
    vehicle = models.TextField(blank=True, null=True)
    attendence = models.BooleanField(default=False, blank=True)        
    calendar_event_id = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created'] 



