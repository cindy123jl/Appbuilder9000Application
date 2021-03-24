from django.shortcuts import render


def home(request):
    return render(request, 'CryptoApp/CryptoApp_home.html')

