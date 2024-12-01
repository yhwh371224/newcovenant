from django.urls import path
from .views import BulletinListView, BulletinDetailView, column_list, column_detail, MemberListView, MemberDetailView


urlpatterns = [
    path('bulletins/', BulletinListView.as_view(), name='bulletin-list'),
    path('bulletins/<int:pk>/', BulletinDetailView.as_view(), name='bulletin-detail'),
    path('columns/', column_list, name='column_list'),
    path('columns/<int:pk>/', column_detail, name='column_detail'),
    path('members/', MemberListView.as_view(), name='member_list'),
    path('members/<int:pk>/', MemberDetailView.as_view(), name='member_detail'),
]