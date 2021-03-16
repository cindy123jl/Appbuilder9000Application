from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {}
    return render(request, 'GardenApp/garden_home.html', context)

def gardenplanner(request):
    context = {}
    return render(request, 'GardenApp/garden_gardenplanner.html', context)

def contact(request):
    context = {}
    return render(request, 'GardenApp/garden_care.html', context)