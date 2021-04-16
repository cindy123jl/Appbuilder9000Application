from django.shortcuts import render, redirect, get_object_or_404
from .models import Stock
from .form import StockForm
import requests

# Create your views here.
def home(request):
    return render(request, 'StockApp/StockApp_home.html')


def base(request):
    return render(request, 'StockApp/StockApp_base.html')


def new(request):
    form = StockForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('StockApp_home')
    content = {'form': form}
    return render(request, 'StockApp/StockApp_newstock.html', content)


def watchlist(request):
    items = Stock.objects.all()
    context = {
        'items': items
    }
    return render(request, 'StockApp/StockApp_Watchlist.html', context)

