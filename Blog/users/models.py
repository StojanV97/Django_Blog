from django.db import models
from PIL import Image
from django.contrib.auth.models import User


class Profile(models.Model):
        user = models.OneToOneField(User,on_delete=models.CASCADE)
        # default image for any user , upload_to - directory where images get uploaded to
        image = models.ImageField(default='default.jpg',upload_to='profile_pics')

        def __str__(self):
            return f'{self.user.username} Profile'

        # Ova Metoda se pokrece kada sacuvamo objekat, pripada klasi models.Model
        # Redefinisemo metodu kako bi pre snimanja profila pormenili velicinu slike
        def save(self, *args, **kwargs):
             super(Profile, self).save(*args, **kwargs)
             img = Image.open(self.image.path)

             if img.height > 300 or img.width > 300 :
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)


# Create your models here.
