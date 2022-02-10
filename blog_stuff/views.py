from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


from .forms import NewTopic
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

def new_topic(request):
    """Novos títulos"""
    if request.method == 'POST':
        form = NewTopic(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog_stuff:titles'))
        
    else:
        form = NewTopic()
        
    context = {'form': form}
    return render(request, 'blog_stuff/new_topic.html', context)
