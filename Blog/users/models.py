from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
        user = models.OneToOneField(User,on_delete=models.CASCADE)
        # default image for any user , upload_to - directory where images get uploaded to
        image = models.ImageField(default='default.jpg',upload_to='profile_pics')

        def __str__(self):
            return f'{self.user.username} Profile'

       # def save(self, *args, **kwargs):
        #     super(Profile, self).save(*args, **kwargs)



# Create your models here.
