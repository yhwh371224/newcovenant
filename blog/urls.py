from django.urls import path
from .views import column_list, column_detail, MemberListView, MemberDetailView


urlpatterns = [
    path('columns/', column_list, name='column-list'),
    path('columns/<int:pk>/', column_detail, name='column-detail'),
    path('members/', MemberListView.as_view(), name='member-list'),
    path('members/<int:pk>/', MemberDetailView.as_view(), name='member-detail'),
]
