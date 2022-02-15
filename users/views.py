from django.shortcuts import render
from django.contrib.auth import logout, login
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def logout_views(request):
    """Realiza o logout da conta"""
    logout(request)
    return HttpResponseRedirect(reverse('blog_stuff:index'))