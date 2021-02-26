from django.http import request
from django.shortcuts import render


def coffee_home(request):
    return render(request, "Coffeeshop/coffee_home.html")
