from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('perfectInfo/', views.perfectInfo, name='perfectInfo'),
    path('seeInfo/', views.seeInfo, name='seeInfo'),
]
