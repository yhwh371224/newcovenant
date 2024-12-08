import os

from django.utils.dateparse import parse_datetime
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.urls import reverse_lazy

from .models import Members, Bulletin
from .forms import BulletinForm
from PyPDF2 import PdfMerger
from datetime import datetime


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
    queryset = Bulletin.objects.all().order_by('-created')
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



def merge_latest_pdfs(request):
    bulletins_folder = "_media/bulletins"
    pdf_files = [os.path.join(bulletins_folder, f) for f in os.listdir(bulletins_folder) if f.endswith('.pdf')]

    if len(pdf_files) < 2:
        return JsonResponse({"status": "error", "message": "병합할 PDF 파일이 충분하지 않습니다. 최소 2개의 PDF 파일이 필요합니다."})

    pdf_files.sort(key=lambda x: os.path.getctime(x), reverse=True)
    latest_files = pdf_files[:2]

    dates = []
    for pdf in latest_files:
        filename = os.path.basename(pdf)
        try:
            date_str = filename.split('_')[0]
            parsed_date = parse_datetime(date_str) or datetime.strptime(date_str, '%Y-%m-%d')
            dates.append(parsed_date)
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"날짜 파싱 오류: {filename}, {str(e)}"})

    latest_date = max(dates)
    merged_filename = latest_date.strftime('%Y-%m-%d') + " 주보 보기.pdf"
    merged_file_path = os.path.join(bulletins_folder, merged_filename)

    merger = PdfMerger()
    for pdf in latest_files:
        merger.append(pdf)
    merger.write(merged_file_path)
    merger.close()

    for pdf in latest_files:
        os.remove(pdf)

    return JsonResponse({"status": "success", "message": f"병합 완료: {merged_file_path}"})

