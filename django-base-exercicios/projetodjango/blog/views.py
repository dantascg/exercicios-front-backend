from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Pessoa

def home(request):
    return render(request, 'home.html')


def testing(request):
  posts = Post.objects.all().values()
  template = loader.get_template('home.html')
  context = {
    'posts': posts,
  }
  return HttpResponse(template.render(context, request))


@login_required
def profile_view(request):
    try:
        pessoa = Pessoa.objects.get(usuario=request.user)
      
        
    except Pessoa.DoesNotExist:
        pessoa = None
        
    context = {
        'user': request.user,      
        'pessoa': pessoa,          
    }
    
    return render(request, 'profile.html', context)

def login_view(request):
    return render(request, 'login.html')

def cadastro_view(request):
    return render(request, 'cadastro.html')


def logout_view(request):
    return render(request, 'logout.html')

def recuperar_view(request):
    return render(request, 'recuperarsenha.html')

def alterarsenha_view(request):
    return render(request, 'alterarsenha.html')

def err404_view(request):
    return render(request, '404.html')

def err403_view(request):
    return render(request, '403.html')

def err500_view(request):
    return render(request, '500.html')