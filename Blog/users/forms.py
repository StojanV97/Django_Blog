from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

'''nasledjujemo UserCreationForm kako bi dodali nasa polja,
    u ovom slucaju to polje je email
'''
class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta: #konfiguracija modela na koji ce se forma odnositi
        model = User
        #polja koja cemo imati u formi
        fields = ['username', 'email', 'password1','password2']


class UserUpdateForm(forms.ModelForm):
        email = forms.EmailField()

        class Meta: #konfiguracija modela na koji ce se forma odnositi
            model = User
            #polja koja cemo imati u formi
            fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields  = ['image']
