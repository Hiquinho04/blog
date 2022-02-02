from django.shortcuts import render
from blog_stuff.models import Title
# Create your views here.
# for a new view use 'def ...'

def index(request):
    """Página inicial"""
    
    return render(request, 'blog_stuff/index.html')

def titles(request):
    """Titulos"""
    titles = Title.objects.order_by('date_added')
    context = {'titles':titles}
    return render(request, 'blog_stuff/titles.html', context)

def texts(request, title_id):
    """Textos"""
    title = Title.objects.get(id=title_id)
    texts = title.text_set.order_by('-date_added')
    context = {'title':title, 'texts':texts}
    return render(request, 'blog_stuff/texts.html', context)
