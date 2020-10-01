from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView,DetailView,CreateView


def home(request):

    return render(request,'blog_app/home.html',{'posts' : Post.objects.all(),
    'title' : 'Home'})

def about(request):
    return HttpResponse("<h1>Blog About</h1>")

class PostListView(ListView):
    model = Post
    template_name = 'blog_app/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts' 
    ordering = ['-date_posted']  # redosled elemenata u listi posts

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
