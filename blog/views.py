from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .models import Members, Column, Bulletin
from .forms import BulletinForm



def column_list(request):
    columns = Column.objects.all().order_by('-created_at')  
    paginator = Paginator(columns, 15)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'columns/column_list.html', {'page_obj': page_obj})


def column_detail(request, pk):
    column = get_object_or_404(Column, pk=pk)
    return render(request, 'columns/column_detail.html', {'column': column})


class MemberListView(ListView):
    model = Members
    template_name = 'members_list.html'
    context_object_name = 'members'


class MemberDetailView(DetailView):
    model = Members
    template_name = 'member_detail.html'
    context_object_name = 'member'


class BulletinListView(ListView):
    model = Bulletin
    template_name = 'bulletins/bulletin_list.html'
    context_object_name = 'bulletins'
    login_url = '/login/'

    def post(self, request, *args, **kwargs):
        form = BulletinForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bulletin_list')  
        return self.get(request, *args, **kwargs)


class BulletinDetailView(DetailView):
    model = Bulletin
    template_name = 'bulletins/bulletin_detail.html'
    context_object_name = 'bulletin'


class BulletinUploadView(LoginRequiredMixin, CreateView):
    model = Bulletin
    form_class = BulletinForm
    template_name = 'blog/bulletin_upload.html'
    success_url = '/blog/bulletins/'  

    def form_valid(self, form):        
        return super().form_valid(form)
    
    def get_login_url(self):
        return f'{super().get_login_url()}?next={self.request.path}'

