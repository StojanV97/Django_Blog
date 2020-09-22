from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author' : 'Stojan',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'Augutst 25, 2015'

    },
        {
        'author' : 'Joe Doe',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'Augutst 25, 2015'

    },
        {
        'author' : 'Doe Joe',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'Augutst 25, 2015'

    }
]

def home(request):

    return render(request,'blog_app/home.html',{'posts' : posts,
    'title' : 'Home'})



def about(request):
    return HttpResponse("<h1>Blog About</h1>")
