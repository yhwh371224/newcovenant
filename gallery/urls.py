from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'gallery'

urlpatterns = [
    path('', views.GalleryList.as_view(), name="gallery"),
    path('create/', views.GalleryCreate.as_view(), name="gallery_create"),
    path('custom_login/', views.custom_login_view, name='custom_login'),
    path('custom_logout/', views.custom_logout_view, name='custom_logout'),
    path('search/<str:q>/', views.GallerySearch.as_view(), name="gallery_search"),
    path('<int:pk>/', views.GalleryDetail.as_view(), name="gallery_detail"),
    path('<int:pk>/update/', views.GalleryUpdate.as_view(), name="gallery_update"),
    path('<int:pk>/new_comment/', views.CommentCreate.as_view(), name='new_comment'),
    path('comment/<int:pk>/update/', views.CommentUpdate.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDelete.as_view(), name='comment_delete'),
]
