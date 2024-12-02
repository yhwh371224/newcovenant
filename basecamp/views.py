from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Bulletin, Column, Members


def index(request): return redirect('/home/')


def home(request): return render(request, 'basecamp/home.html')


def about_us(request): return render(request, 'basecamp/about_us.html')


@login_required
def confirmation(request): 
    return render(request, 'basecamp/confirmation.html')


def information(request):     
    return render(request, 'basecamp/information.html')


def introduction(request):     
    return render(request, 'basecamp/introduction.html')



def bulletin_list(request):     
    return render(request, 'basecamp/bulletin_list.html')


def meetings(request):     
    return render(request, 'basecamp/meetings.html')


def meeting_point(request): 
    return render(request, 'basecamp/meeting_point.html')


def payment_options(request): 
    return render(request, 'basecamp/payment_options.html')


def payonline(request):     
    return render(request, 'basecamp/payonline.html')


def payonline_stripe(request):     
    return render(request, 'basecamp/payonline_stripe.html')


def sitemap(request): 
    return render(request, 'basecamp/sitemap.xml')


def workers(request): 
    return render(request, 'basecamp/workers.html')


def column(request):
    return render(request, 'basecamp/column.html')


def gallery(request):
    return render(request, 'basecamp/gallery.html')


def location(request):
    return render(request, 'basecamp/location.html')


def pickup(request):
    return render(request, 'basecamp/pickup.html')


def worship_music(request):
    return render(request, 'basecamp/worship_music.html')


# def bulletin_list(request):
#     bulletins = Bulletin.objects.all()
#     return render(request, 'bulletin_list.html', {'bulletins': bulletins})


