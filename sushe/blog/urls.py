from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='blog'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('about/', views.about, name='about'),
    path('context/', views.context, name='context'),
]