from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # auto_now_add=True - postavice datum u trenutku kreiranja objekta, ne moze se dodanji izmeniti
    date_posted = models.DateTimeField(default=timezone.now)
    # koristimo ForeignKey da bi mapirali Usera sa Postomx
    # on_delete=CASCADE - obrisanje post kada se obrise i korisnik
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

