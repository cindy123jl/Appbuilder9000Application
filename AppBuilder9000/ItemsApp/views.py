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
            return redirect('home')
    content = {'form': form}
    return render(request, 'ItemsApp/new_item.html', content)


def createItem(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        print(form.errors)
        form = ItemForm()
    context = {
        'form': form,
    }
    return render(request, 'ItemsApp/createItem.html', context)


def viewItem(request):
    return render(request, 'ItemsApp/displayItems.html')


def details(request, pk):
    items = Item.objects.all()
    return render(request, 'ItemsApp/displayItems.html', {'items': items})
