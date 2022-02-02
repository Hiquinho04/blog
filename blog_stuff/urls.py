from django.urls import path, include
from . import views

#urls internas 
urlpatterns = [
    path('', views.index, name='index')
    
]