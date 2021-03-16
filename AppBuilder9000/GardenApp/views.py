from django.shortcuts import render, redirect
from .forms import PlannerForm



# Create your views here.
def home(request):
    context = {}
    return render(request, 'GardenApp/garden_home.html', context)


def gardenplanner(request):
    context= {}
    return render(request, 'GardenApp/garden_gardenplanner.html', context)


def care(request):
    context = {}
    return render(request, 'GardenApp/garden_care.html', context)


def createplanner(request):
    if request.method == 'POST':
        form = PlannerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gardenplanner')
    else:
        form = PlannerForm()
        return render(request, 'GardenApp/garden_gardenplanner.html', {'form': form})  # pass form to render on gardenplanner.html
