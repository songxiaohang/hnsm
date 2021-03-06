"""sushe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views
# RSS功能
from blog.feeds import AllPostsRssFeed


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    # django默认提供登录代码,默认登录界面是registration/login.html
    path('users/', include('django.contrib.auth.urls')),
    # 首页视图
    path('', views.index, name='index'),
    path('blog/', include('blog.urls')),
    path('', include('comments.urls')),
    path('all/rss/', AllPostsRssFeed(), name='rss'),
    # django3 暂不支持 django-haystack搜索引擎
    # path('search/', include('haystack.urls')),
]
