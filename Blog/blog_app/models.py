from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    #python manage.py sqlmigrate blog_app 0001
    #python manage.py migrations
    #python manage.py shell
    #python manage.py makemigrations

    title = models.CharField(max_length=100)
    content = models.TextField()
    # auto_now_add=True - postavice datum u trenutku kreiranja objekta, ne moze se dodanji izmeniti
    date_posted = models.DateTimeField(default=timezone.now)
    # koristimo ForeignKey da bi mapirali Usera sa Postomx
    # on_delete=CASCADE - obrisanje post kada se obrise i korisnik
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # koristimo reverse kako bi nam vratio url na koji ce se preusmeriti nakon submitovane forme
        # reverse samo vraca putanju kao string, predefinisana forma u view-u obavlja preusmeravanje
        return reverse('post-detail', kwargs={'pk':self.pk}) 
