import json
import requests

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.http import JsonResponse

from .models import Gallery, Comment
from .forms import CommentForm, GalleryForm
from blog.models import Members 
from main.settings import RECIPIENT_EMAIL


class GalleryList(ListView):
    model = Gallery
    template_name = 'gallery/gallery_list.html'
    paginate_by = 7

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GalleryList, self).get_context_data(**kwargs)
        context['gallery_count'] = Gallery.objects.all().count()

        email = self.request.session.get('email', None)
        if email:
            blog_gallery = Members.objects.filter(email=email).first()  
            if blog_gallery:
                user_name = blog_gallery.name
                context['user_name'] = user_name
            else:
                context['user_name'] = None
        else:
            context['user_name'] = None

        context['email'] = email 
        context['search_error'] = self.request.session.get('search_error', None)  

        return context
    

class GalleryCreate(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:  # 로그인된 사용자 확인
            form = GalleryForm(initial={'name': request.user.name})
        else:
            form = GalleryForm()
        return render(request, 'gallery/Gallery_form.html', {'form': form, 'form_guide': 'Please Gallery your gallery'})

    def Gallery(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('gallery:custom_login')  # 로그인 페이지로 리다이렉트

        form = GalleryForm(request.Gallery)
        if form.is_valid():
            form.instance.author = request.user.name
            form.instance.name = request.user.name
            form.save()
            return redirect('/gallery/')
        return render(request, 'gallery/gallery_form.html', {'form': form, 'form_guide': 'Please Gallery your gallery'})


class GalleryDetail(DetailView):
    model = Gallery
    template_name = 'gallery/gallery_detail1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery_count'] = Gallery.objects.all().count()
        context['comment_form'] = CommentForm()

        email = self.request.session.get('email', None)
        context['email'] = email

        if email:
            blog_gallery = Members.objects.filter(email=email).first()  
            if blog_gallery:
                user_name = blog_gallery.name
                context['user_name'] = user_name
            else:
                context['user_name'] = None
        else:
            context['user_name'] = None

        return context
        

class GalleryUpdate(UpdateView):
    model = Gallery
    template_name = 'gallery/gallery_form.html'
    fields = ['content', 'title']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        email = self.request.session.get('email', None)
        context['email'] = email

        if email:
            blog_gallery = Members.objects.filter(email=email).first()  
            if blog_gallery:
                user_name = blog_gallery.name
                context['user_name'] = user_name
            else:
                context['user_name'] = None
        else:
            context['user_name'] = None

        return context
       

def index(request):
    Gallerys = Gallery.objects.all()
    return render(request, 'gallery/index.html', {'Gallerys': Gallerys})
