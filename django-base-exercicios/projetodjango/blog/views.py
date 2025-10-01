from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def home(request):
    return render(request, 'home.html')


def testing(request):
  posts = Post.objects.all().values()
  template = loader.get_template('home.html')
  context = {
    'posts': posts,
  }
  return HttpResponse(template.render(context, request))