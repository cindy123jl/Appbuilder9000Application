from django.shortcuts import render, redirect, get_object_or_404
from .forms import RestaurantForm, DishForm
from .models import Restaurant, Dish


def MyThai_home(request):
    return render(request, 'MyThai/MyThai_home.html')


def new_restaurant(request):
    form = RestaurantForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('MyThai_my_restaurants')
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
            return redirect('MyThai_my_restaurants')
        else:
            content = {'form': form}
            return render(request, 'MyThai/MyThai_add_dish.html', content)
    content = {'form': form}
    return render(request, 'MyThai/MyThai_add_dish.html', content)


def my_restaurants(request):
    restaurants = Restaurant.objects.all()
    dishes = Dish.objects.all()
    return render(request, 'MyThai/MyThai_my_restaurants.html', {'restaurants': restaurants, 'dishes': dishes})


# def display_restaurants(request, pk):
#     pk = int(pk)
#     restaurant = get_object_or_404(Restaurant, pk=pk)
#     form = RestaurantForm(data=request.POST or None, instance=restaurant)
#     if request.method == 'POST':
#         if form.is_valid():
#             form2 = form.save(commit=False)
#             form2.save()
#             return redirect('')