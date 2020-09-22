from django.urls import path
from . import views

urlpatterns = [
    #  name koristimo da bi mogli da prosledimo putanju u html templejtu
    # { url 'blog-home' }
    path('', views.home, name='blog-home'),
    path('about/',views.about,name='blog-about'),
]
