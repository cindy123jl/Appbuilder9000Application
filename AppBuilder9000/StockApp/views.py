from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'StockApp/StockApp_home.html')


def base(request):
    return render(request, 'StockApp/StockApp_base.html')
