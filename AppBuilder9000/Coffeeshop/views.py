from django.shortcuts import render
from .models import Drink
from .forms import DrinkForm
from django.http import HttpResponseRedirect


def coffee_home(request):
    return render(request, "Coffeeshop/coffee_home.html")


def current_drinks(request):
    form = DrinkForm()
    posts = Drink.objects.all()
    print(posts)

    return render(request, "Coffeeshop/current_drinks.html")


def drink_menu(request):
    form = DrinkForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'Coffeeshop/drink_menu.html', {'form': form})
