from django.contrib import admin
from .models import Post


admin.site.register(Post) # da bi videli model na admin stranici moramo ga registrovati
