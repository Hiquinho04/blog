"""Urls do app users"""
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'),
                name='login'),
    #views.logout é uma função NÃO USAR
    path('logout/', views.logout_views, name='logout'),
    path('register/', views.register, name='register'),
    
]