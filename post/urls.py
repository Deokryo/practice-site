from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name = 'post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('like/<int:pk>/', views.likes, name='likes'),
    path('post/<int:a>/delete/<int:pk>/', views.comment_delete, name='comment_delete'),
    path('post/<int:pk>/delete', views.post_delete, name ='post_delete'),
    path('my_page/<int:pk>/', views.profile, name='my_page'),
    path('my_page/<int:pk>/edit/', views.profile_edit,name='profile_edit'),
]   