from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    #path('<int:main.main_group.id>/', views.view_group, name='group'),
]