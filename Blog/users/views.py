from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request,f'Your Account Has Been Created, You Can Login Now!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request,'users/register.html',{'form':form})

#dekorator dodaje funkcionalnost funkciji
@login_required
def profile(request):
    return render(request,'users/profile.html')
    #korisnika ne moramo da prosledjujemo templejtu jer django sadrzi user promenljivu koja predstavlja trenutno ulogovanog korisnika
