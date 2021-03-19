from django.shortcuts import render, redirect
from .forms import PlannerForm, EvalForm
from .models import Planner



# Create your views here.
def home(request):
    context = {}
    return render(request, 'GardenApp/garden_home.html', context)


def gardenplanner(request):
    context= {}
    return render(request, 'GardenApp/garden_gardenplanner.html', context)





def createplanner(request):
    if request.method == 'POST':
        form = PlannerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gardenplanner')
        else:
            form = PlannerForm(request.POST)
            return render(request, 'GardenApp/garden_gardenplanner.html', {'form': form})  # pass form to render on gardenplanner.html
    else:
        form = PlannerForm(None)
        return render(request, 'GardenApp/garden_gardenplanner.html', {'form': form})

def createevalform(request):
    if request.method == 'POST':
        form = EvalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gardenplanner')
        else:
            form = EvalForm()
            return render(request, 'GardenApp/garden_tracking.html', {'form': form})
    else:
        form = EvalForm(None)
        return render(request, 'GardenApp/garden_tracking.html', {'form': form})



def get_gardenplanner(request):
    preseason = Planner.objects.all()
    context = {'preseason': preseason}
    return render(request, 'GardenApp/garden_care.html', context)