from django.shortcuts import render, redirect, get_object_or_404
from .models import Currency, CoinStatus
from .forms import CurrencyForm, CoinStatusForm


def home(request):
    return render(request, 'CryptoApp/CryptoApp_home.html')


def add_currency(request):
    form = CurrencyForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('CryptoApp_home')
    content = {'form': form}
    return render(request, 'CryptoApp/CryptoApp_AddCurrency.html', content)

