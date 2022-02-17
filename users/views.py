from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def logout_views(request):
    """Realiza o logout da conta"""
    logout(request)
    return HttpResponseRedirect(reverse('blog_stuff:index'))

def register(request):
    """Formulário de novo usuário, recebe o request"""

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            
            new_user = form.save()
            authenticate_user = authenticate(username=new_user.username,
                        password=request.POST['password1'])
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse('blog_stuff:index'))

        context = {'form':form}
        return render(request, 'users/register.html', context)

    else:
        return render(request, 'users/register.html', {'form':UserCreationForm()})
