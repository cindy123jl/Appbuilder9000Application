from django.shortcuts import render, redirect
from .forms import RestaurantForm, DishForm


def MyThai_home(request):
    return render(request, 'MyThai/MyThai_home.html')


def new_restaurant(request):
    form = RestaurantForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('MyThai_home')
        else:
            content = {'form': form}
            return render(request, 'MyThai/MyThai_add_restaurant.html', content)
    content = {'form': form}
    return render(request, 'MyThai/MyThai_add_restaurant.html', content)


def new_dish(request):
    form = DishForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('MyThai_home')
        else:
            content = {'form': form}
            return render(request, 'MyThai/MyThai_add_dish.html', content)
    content = {'form': form}
    return render(request, 'MyThai/MyThai_add_dish.html', content)
