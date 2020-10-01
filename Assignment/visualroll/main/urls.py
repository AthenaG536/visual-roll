from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('group/<int:group_id>/', views.view_group, name='group'),
    path('photo/<int:photo_id>/', views.view_photo, name='photo'),
    path('photo/<int:member_id>/', views.members, name='member'),
]