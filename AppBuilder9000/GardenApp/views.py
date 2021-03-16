from django.shortcuts import render
from .forms import PlannerForm


# Create your views here.
def home(request):
    context = {}
    return render(request, 'GardenApp/garden_home.html', context)


def gardenplanner(request):
    context = {}
    return render(request, 'GardenApp/garden_gardenplanner.html', context)


def care(request):
    context = {}
    return render(request, 'GardenApp/garden_care.html', context)


def createplanner(request):
    form = PlannerForm()  # instance of planner form
    return render(request, 'GardenApp/garden_gardenplanner.html', {'form': form})  # pass form to render on gardenplanner.html
