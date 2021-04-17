from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RestaurantForm, DishForm
from .models import Restaurant, Dish
from operator import attrgetter


def MyThai_home(request):
    return render(request, 'MyThai/MyThai_home.html')


def new_restaurant(request):
    # Store Restaurant form as form
    form = RestaurantForm(data=request.POST or None)
    if request.method == 'POST':
        # If form is valid save and return to dishes page.
        if form.is_valid():
            form.save()
            return redirect('MyThai_my_restaurants')
        else:
            # If form isn't valid return to the add page with the content entered.
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


def my_restaurants_view(request):
    restaurant_list = Restaurant.objects.all()
    dish_list = Dish.objects.all()

    get_dish_query = request.GET.get('get_dish')
    my_sort = request.GET.get('dishes')

    if is_valid_query(get_dish_query):  # If is valid = True, filter queryset
        dish_list = dish_list.filter(
            Q(dishName__icontains=get_dish_query) |
            Q(restaurant__name__icontains=get_dish_query)).distinct()  # Only return distinct entries

    if my_sort is None:
        my_sort = 'dishName'

    dish_list = my_sorted(dish_list, my_sort)  # Sort Dict

    paginator1 = Paginator(restaurant_list, 10)  # Create paginator object with 10 restaurants per page
    paginator2 = Paginator(dish_list, 15)

    page = request.GET.get('page')  # Store paginator object with page number

    restaurants = paginator1.get_page(page)
    dishes = paginator2.get_page(page)

    context = {'restaurants': restaurants, 'dishes': dishes}
    return render(request, 'MyThai/MyThai_my_restaurants.html', context)


def is_valid_query(param):
    return param != '' and param is not None  # Makes sure search is valid query, if not return false


def my_sorted(dish_list, my_sort):
    if my_sort == 'rating':  # If sorted by rating, reverse so highest goes at the top.
        asc = True
    else:
        asc = False
    dish_list = sorted(dish_list, key=attrgetter(my_sort), reverse=asc)  # Sort dict by model attribute = 'my_sort'
    return dish_list


def details(request, pk):
    pk = int(pk)
    dish = get_object_or_404(Dish, pk=pk)
    context = {'dish': dish}
    return render(request, 'MyThai/MyThai_details.html', context)
