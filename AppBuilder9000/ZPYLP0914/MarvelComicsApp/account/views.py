from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm

def registration_view(request):
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('MarvelComicsAppHome')
        else:
            form = RegistrationForm()
    else:
        form = RegistrationForm()
    return render(request, 'account/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('MarvelComicsAppHome')

def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('MarvelComicsAppHome')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('MarvelComicsAppHome')

    else:
        form = AccountAuthenticationForm()

    return render(request, 'account/login.html', {'form': form})
