from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
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
        if request.method == 'POST':
            # instanciramo formu sa podacima korisnika tako sto prosledimo instancu korisnika
            # request.POST su podaci kojima cemo updejtovati formu
            # request.FILES se ubacuje zato sto postoji slika koju korisnik uploaduje
            u_form = UserUpdateForm(request.POST,
                request.FILES,
                instance=request.user)
            p_form = ProfileUpdateForm(request.POST,
                request.FILES,
                instance=request.user.profile)
            if u_form.is_valid() and  p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request,f'Your Account Has Been Updated')
                return redirect('profile')
        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)

        return render(request,'users/profile.html', { 'u_form' : u_form , 'p_form' : p_form })
        #korisnika ne moramo da prosledjujemo templejtu jer django sadrzi user promenljivu koja predstavlja trenutno ulogovanog korisnika

