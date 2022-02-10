from django.urls import path, include
from . import views

#urls internas 
urlpatterns = [
    path('', views.index, name='index'),
    path('titles/', views.titles, name='titles'),
    path('titles/<int:title_id>/', views.texts, name='texts'),
    path('new_topic/', views.new_topic, name='new_topic'),

]