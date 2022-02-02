from django.shortcuts import render

# Create your views here.
# for a new view use 'def ...'

def index(request):
    """Página inicial"""
    
    return render(request, 'blog_stuff/index.html')