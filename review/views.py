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
from django.contrib.auth import authenticate, login, logout

from .models import Post, Comment
from .forms import CommentForm, PostForm
from blog.models import Members 
from main.settings import RECIPIENT_EMAIL


def custom_login_view(request):
    error = None
    if request.method == 'POST':
        email = request.POST.get('email')
        user = authenticate(request, email=email)  
        if user:
            login(request, user)  
            return redirect('review:review')  
        else:
            error = 'This is not the email address in our system'

    return render(request, 'review/custom_login.html', {'error': error})


def custom_logout_view(request):
    logout(request)  # 세션 비우기    
    return redirect('review:review')


def get_authenticated_post(request):
    email = request.session.get('email')
    if email:
        posts = Members.objects.filter(email=email)
        if posts.exists():
            return posts.first()  
    return None


class PostList(ListView):
    model = Post
    template_name = 'review/post_list.html'
    paginate_by = 7

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['post_count'] = Post.objects.all().count()

        authenticated_post = get_authenticated_post(self.request)
        context['authenticated_post'] = authenticated_post 

        email = self.request.session.get('email', None)
        if email:
            blog_post = Members.objects.filter(email=email).first()  
            if blog_post:
                user_name = blog_post.name
                context['user_name'] = user_name
            else:
                context['user_name'] = None
        else:
            context['user_name'] = None

        context['email'] = email 
        context['search_error'] = self.request.session.get('search_error', None)  

        return context
    

class PostCreate(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:  # 로그인된 사용자 확인
            form = PostForm(initial={'name': request.user.name})
        else:
            form = PostForm()
        return render(request, 'review/post_form.html', {'form': form, 'form_guide': 'Please post your review'})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('review:custom_login')  # 로그인 페이지로 리다이렉트

        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user.name
            form.instance.name = request.user.name
            form.save()
            return redirect('/review/')
        return render(request, 'review/post_form.html', {'form': form, 'form_guide': 'Please post your review'})
    

class PostSearch(PostList):
    def get_queryset(self):
        q = self.kwargs['q']
        object_list = Post.objects.filter(Q(name__contains=q) | Q(content__contains=q)) 
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostSearch, self).get_context_data(object_list=object_list, **kwargs)  
        context['search_info'] = 'Search: "{}"'.format(self.kwargs['q'])
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'review/post_detail1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_count'] = Post.objects.all().count()
        context['comment_form'] = CommentForm()

        email = self.request.session.get('email', None)
        context['email'] = email

        authenticated_post = get_authenticated_post(self.request)
        context['authenticated_post'] = authenticated_post 

        if email:
            blog_post = Members.objects.filter(email=email).first()  
            if blog_post:
                user_name = blog_post.name
                context['user_name'] = user_name
            else:
                context['user_name'] = None
        else:
            context['user_name'] = None

        return context
        

class PostUpdate(UpdateView):
    model = Post
    template_name = 'review/post_form.html'
    fields = ['content', 'title']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        email = self.request.session.get('email', None)
        context['email'] = email

        authenticated_post = get_authenticated_post(self.request)
        context['authenticated_post'] = authenticated_post 

        if email:
            blog_post = Members.objects.filter(email=email).first()  
            if blog_post:
                user_name = blog_post.name
                context['user_name'] = user_name
            else:
                context['user_name'] = None
        else:
            context['user_name'] = None

        return context
    

class CommentCreate(View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        email = request.session.get('email', None)

        user_name = None
        if email:
            blog_post = Members.objects.filter(email=email).first()
            if blog_post:
                user_name = blog_post.name

        comment_form = CommentForm()
        
        context = {
            'post': post,
            'email': email,
            'user_name': user_name,
            'comment_form': comment_form,
        }

        return render(request, 'review/post_detail1.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        email = request.session.get('email', None)

        user_name = None
        if email:
            blog_post = Members.objects.filter(email=email).first()
            if blog_post:
                user_name = blog_post.name

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = user_name
            comment.save()
            return redirect(post.get_absolute_url())  # Redirect to post detail page

        # Render the form with errors if form is not valid
        context = {
            'post': post,
            'email': email,
            'user_name': user_name,
            'comment_form': comment_form,
        }
        return render(request, 'review/post_detail1.html', context)
    

class CommentUpdate(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'review/comment_form.html'

    def get_object(self, queryset=None):
        comment = super().get_object(queryset)        
        email = self.request.session.get('email', None)
        user_name = None

        if email:
            blog_post = Members.objects.filter(email=email).first()
            if blog_post:
                user_name = blog_post.name

        if comment.author != user_name:
            raise PermissionDenied('No right to edit')

        return comment
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        email = self.request.session.get('email', None)
        user_name = None

        if email:
            blog_post = Members.objects.filter(email=email).first()
            if blog_post:
                user_name = blog_post.name

        context['email'] = email
        context['user_name'] = user_name
        return context

    def get_success_url(self):
        post = self.get_object().post
        return post.get_absolute_url() + '#comment-list'


class CommentDelete(DeleteView):
    model = Comment
    template_name = 'review/comment_confirm_delete.html'

    def get_object(self, queryset=None):
        comment = super().get_object(queryset)        
        email = self.request.session.get('email', None)
        user_name = None

        if email:
            blog_post = Members.objects.filter(email=email).first()
            if blog_post:
                user_name = blog_post.name

        if comment.author != user_name:
            raise PermissionDenied('No right to delete Comment')

        return comment
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        email = self.request.session.get('email', None)
        user_name = None

        if email:
            blog_post = Members.objects.filter(email=email).first()
            if blog_post:
                user_name = blog_post.name

        context['email'] = email
        context['user_name'] = user_name
        return context

    def get_success_url(self):
        post = self.get_object().post
        return post.get_absolute_url() + '#comment-list'
    

def index(request):
    posts = Post.objects.all()
    return render(request, 'review/index.html', {'posts': posts})
