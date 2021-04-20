from django.shortcuts import render, redirect, get_object_or_404
from .form import StockForm
from .models import WatchStock


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
    all_stocks = WatchStock.objects.all()
    context = {'all_stocks': all_stocks}
    return render(request, "StockApp/StockApp_Watchlist.html", context)


def details(request, pk):
    pk = pk
    this_stock = WatchStock.objects.filter(pk=pk)
    all_stocks = {'this_stock': this_stock}
    context = this_stock
    return render(request, "StockApp/StockApp_Details.html", context)

#   def detail(request):
#      return render(request, "StockApp/StockApp_Details.html")
