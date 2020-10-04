from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    # TODO: swap home and index templates around to be accurate.
    path(r'', views.home, name='index'),
    path(r'home/', views.index, name='home'),
    path(r'login/', views.login, name='login'),
    path(r'register/', views.UserCreate.as_view(), name='register'),
    path(r'account/<int:pk>/', views.UserView.as_view(), name='user'),
    path(r'<int:user_id>/mygroups/', views.user_groups, name='user_groups'),
    path(r'group/<int:group_id>', views.group_detail, name='group'),
    path(r'photo/<int:photo_id>/', views.view_photo, name='photo'),
]