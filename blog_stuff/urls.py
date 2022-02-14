from django.urls import re_path, path, include
from . import views

#urls internas 
urlpatterns = [
    path('', views.index, name='index'),
    path('titles/', views.titles, name='titles'),
    path('titles/<int:title_id>/', views.texts, name='texts'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:title_id>/', views.new_entry, name='new_entry'),
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),


]