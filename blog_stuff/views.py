from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .forms import NewTopic, New_Entry
from blog_stuff.models import Title, Text


# Create your views here.
# for a new view use 'def ...'

def index(request):
    """Página inicial"""
    
    return render(request, 'blog_stuff/index.html')

@login_required
def titles(request):
    """Titulos"""
    titles = Title.objects.filter(owner=request.user).order_by('date_added')
    context = {'titles':titles}
    return render(request, 'blog_stuff/titles.html', context)

@login_required
def texts(request, title_id):
    """Textos"""
    title = Title.objects.get(id=title_id)
    texts = title.text_set.order_by('-date_added')
    # Verifica se o usuario esta acessando um link proprio
    check_user(request, title)

    context = {'title':title, 'texts':texts}
    return render(request, 'blog_stuff/texts.html', context)

@login_required
def new_topic(request):
    """Novos títulos"""
    if request.method == 'POST':
        form = NewTopic(request.POST)
        if form.is_valid():
            # Adicionando o usuario no form
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('blog_stuff:titles'))
        
    else:
        form = NewTopic()
        
    context = {'form': form}
    return render(request, 'blog_stuff/new_topic.html', context)

@login_required
def new_entry(request, title_id):
    """Entradas em cada tópico"""
    title = Title.objects.get(id = title_id)

    check_user(request, title)

    if request.method == 'POST':
        form = New_Entry(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.title = title
            new_entry.save()
            return HttpResponseRedirect(reverse('blog_stuff:texts', args=[title_id]))
    else:
        form = New_Entry()

    context = {'title': title, 'form': form} 
    return render(request, 'blog_stuff/new_entry.html', context)   

@login_required
def edit_entry(request, entry_id):
    """Edita as entradas"""
    text = Text.objects.get(id=entry_id)
    title = text.title

    check_user(request, title)

    if request.method == 'POST':
        form = New_Entry(instance=text, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog_stuff:texts', args=[title.id]))
    else:
        form = New_Entry(instance=text)

    context={'text':text, 'title':title, 'form':form}
    return render(request, 'blog_stuff/edit_entry.html', context)

def check_user(request, title):
    if title.owner != request.user:
        raise Http404