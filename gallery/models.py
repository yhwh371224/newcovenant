from django.db import models
from django.contrib.auth.models import User
from markdownx.utils import markdown


class Gallery(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField(blank=True, null=True)
    head_image = models.ImageField(upload_to='gallery/%Y/%m/%d/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created', ]

    def __str__(self):
        return '{} :: {}'.format(self.title, self.author)

    def get_absolute_url(self):
        return '/gallery/{}/'.format(self.pk)

    def get_update_url(self):
        return self.get_absolute_url() + 'update/'

    def get_markdown_content(self):
        return markdown(self.content)



