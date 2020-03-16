from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    # path('', views.index, name='blog'),
    path('', views.IndexView.as_view(), name='blog'),

    # path('posts/<int:pk>/', views.detail, name='detail'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='detail'),

    path('about/', views.about, name='about'),
    path('context/', views.context, name='context'),

    #path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('archives/<int:year>/<int:month>/', views.ArchiveView.as_view(), name='archive'),

    # path('categories/<int:pk>/', views.category, name='category'),
    path('categories/<int:pk>/', views.CategoryView.as_view(), name='category'),

    # path('tags/<int:pk>/', views.tag, name='tag'),
    path('tags/<int:pk>/', views.TagView.as_view(), name='tag'),

    # 简单搜索
    path('search/', views.search, name='search'),
]