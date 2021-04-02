from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemForm
from .models import Item


# Create your views here.
def home(request):
    return render(request, 'ItemsApp/itemsapp_home.html')


def new_item(request):
    form = ItemForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('itemsApp_home')
    content = {'form': form}
    return render(request, 'ItemsApp/new_item.html', content)
