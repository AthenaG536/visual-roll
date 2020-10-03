from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'account/<int:user_id>/', views.user_detail, name='user'),
    path(r'<int:user_id>/mygroups/', views.user_groups, name='user_groups'),
    path(r'group/<int:group_id>', views.group_detail, name='group'),
    path(r'photo/<int:photo_id>/', views.view_photo, name='photo'),
    path(r'group/<int:group_id>/', views.group_detail, name='group'),
    path(r'photo/<int:photo_id>/', views.view_photo, name='photo'),
]