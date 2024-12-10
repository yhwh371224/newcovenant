from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Bulletin, Members


def index(request): return redirect('/home/')


def home(request): return render(request, 'basecamp/home.html')


def introduction(request):     
    return render(request, 'basecamp/introduction.html')


def bulletin_list(request):     
    return render(request, 'basecamp/bulletin_list.html')


def meetings(request):     
    return render(request, 'basecamp/meetings.html')


def sitemap(request): 
    return render(request, 'basecamp/sitemap.xml')


def workers(request): 
    return render(request, 'basecamp/workers.html')


def column(request):
    return render(request, 'basecamp/column.html')


def location(request):
    return render(request, 'basecamp/location.html')


def contact_list(request):
    return render(request, 'basecamp/contact_list.html')


def worship_music(request):
    return render(request, 'basecamp/worship_music.html')




