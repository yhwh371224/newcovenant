from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


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



def church_bulletin(request):     
    return render(request, 'basecamp/church_bulletin.html')


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


