from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .models import Members, Bulletin
from .forms import BulletinForm
from django.urls import reverse_lazy


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
    template_name = 'blog/bulletin_list.html'
    context_object_name = 'bulletins'
    queryset = Bulletin.objects.all().order_by('-date')
    paginate_by = 4 
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BulletinForm()  # 폼을 컨텍스트에 추가
        return context

    def post(self, request, *args, **kwargs):
        form = BulletinForm(request.POST, request.FILES)  
        
        if form.is_valid():
            form.save()
            return redirect('bulletin_list')  

        return self.render_to_response(self.get_context_data(form=form))
    

class BulletinDetailView(DetailView):
    model = Bulletin
    template_name = 'bulletins/bulletin_detail.html'
    context_object_name = 'bulletin'


class BulletinUploadView(LoginRequiredMixin, CreateView):
    model = Bulletin
    form_class = BulletinForm
    template_name = 'blog/bulletin_upload.html'
    success_url = reverse_lazy('bulletin_list') 

    def form_valid(self, form):        
        return super().form_valid(form)
    
    def get_login_url(self):
        return f'{super().get_login_url()}?next={self.request.path}'
    

