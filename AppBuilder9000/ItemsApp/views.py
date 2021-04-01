from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'ItemsApp/home.html')


def new_item(request):
    return render(request, 'ItemsApp/new_item.html')
