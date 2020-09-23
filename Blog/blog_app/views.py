from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):

    return render(request,'blog_app/home.html',{'posts' : Post.objects.all(),
    'title' : 'Home'})



def about(request):
    return HttpResponse("<h1>Blog About</h1>")
