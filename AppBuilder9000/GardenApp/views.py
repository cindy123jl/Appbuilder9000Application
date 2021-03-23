from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlannerForm, TrackerForm
from .models import Planner, Tracker



# Create your views here.
def home(request):
    context = {}
    return render(request, 'GardenApp/garden_home.html', context)


def createplanner(request):
    if request.method == 'POST':
        form = PlannerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gardenplanner')
        else:
            form = PlannerForm(request.POST)
            return render(request, 'GardenApp/garden_planner.html',
                          {'form': form})  # pass form to render on gardenplanner.html
    else:
        form = PlannerForm(None)
        return render(request, 'GardenApp/garden_planner.html', {'form': form})


def createtracker(request):
    if request.method == 'POST':
        form = TrackerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gardentracker')
        else:
            form = TrackerForm()
            return render(request, 'GardenApp/garden_tracker.html', {'form': form})
    else:
        form = TrackerForm(None)
        return render(request, 'GardenApp/garden_tracker.html', {'form': form})


def allvegetables(request):
    plan = Planner.objects.all()
    track = Tracker.objects.all()
    context = {'plan': plan, 'track': track}
    return render(request, 'GardenApp/garden_allvegetables.html', context)


def vegetabledetails(request, pk):
    pk = int(pk)
    plan = get_object_or_404(Planner, pk=pk)
    track = Tracker.objects.all()
    context = {'plan': plan, 'track': track}
    return render(request, 'GardenApp/garden_details.html', context)


def vegetableedit(request, pk):
    pk = int(pk)
    plan = get_object_or_404(Planner, pk=pk)
    form = PlannerForm(request.POST or None, instance=plan)
    if request.method == "POST":
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('vegetabledetails', pk)
    else:
        return render(request, 'GardenApp/garden_edit.html', {'plan':plan, 'form': form})

