from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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
    paginate_by = 4

class UserPostListView(ListView):
    model = Post
    template_name = 'blog_app/user_post.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts' 
    #ordering = ['-date_posted']  # redosled elemenata u listi posts
    paginate_by = 4

    def get_queryset(self):
        # self.kwargs.get() - uzimamo username iz urla , kwargs sadrzi parametre upita (query)
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        #Calls get() on a given model manager, but it raises Http404 instead of the model’s DoesNotExist exception.
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    
    
# nasledjuje LoginRequieredMixin da bi sprecili pristup ruti ukoliko korisnik nije ulogovan
# kod function based views-a se ovo resava dekoratorima (@LoginRequired)
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# UserPassesTestMixin je provera da li je korisnik koji pokusava da edituje post autor tog posta
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    
