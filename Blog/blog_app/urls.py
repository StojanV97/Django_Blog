from django.urls import path
from .views import PostListView,PostDetailView, PostCreateView,PostUpdateView,PostDeleteView
from . import views

urlpatterns = [
    #  name koristimo da bi mogli da prosledimo putanju u html templejtu
    # { url 'blog-home' }
    path('',PostListView.as_view(), name='blog-home'),
    # pk je primary key koji django ocekuje kako bi preuzeo taj elemenat iz liste, mozemo postaviti bilo koji atribut, defaulitni je pk
    path('post/<int:pk>',PostDetailView.as_view(), name='post-detail'),
    path('post/new',PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post-delete'),
    path('about/',views.about,name='blog-about'),


]
