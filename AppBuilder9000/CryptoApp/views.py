from django.shortcuts import render, redirect
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


def add_status(request):
    form = CoinStatusForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('CryptoApp_home')
    content = {'form': form}
    return render(request, 'CryptoApp/CryptoApp_AddStatus.html', content)


def display(request):
    cryptos = CoinStatus.CoinStatuses.all()
    context = {'cryptos': cryptos}
    return render(request, 'CryptoApp/CryptoApp_display.html', context)


def details(request, record_id):
    coins = CoinStatus.CoinStatuses.filter(id=record_id)
    this_coin = coins[0]
    # Create dictionary for use on details page
    coin_detail = {
        'coin_name': this_coin.currency.chain_name,
        'coin_unit': this_coin.currency.coin_unit,
        'chain_type': this_coin.currency.chain_type,
        'launch_year': this_coin.currency.launch_year,
        'value': this_coin.value,
        'as_of_date': this_coin.as_of_date,
        'supply': this_coin.supply,
        'market_cap': this_coin.market_cap,
        'transactions_per_sec': this_coin.transactions_per_sec
    }
    context = {'coin_detail': coin_detail}
    return render(request, 'CryptoApp/CryptoApp_details.html', context)

