from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlannerForm, EvalForm
from .models import Planner, Eval
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.
def home(request):
    context = {}
    return render(request, 'GardenApp/garden_home.html', context)


def gardenplanner(request):
    context = {}
    return render(request, 'GardenApp/garden_gardenplanner.html', context)

def gardensearch(request):
    context = {}
    return render(request, 'GardenApp/garden_search.html', context)

def gardendetails(request):
    context = {}
    return render(request, 'GardenApp/garden_details.html', context)


def createplanner(request):
    if request.method == 'POST':
        form = PlannerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gardenplanner')
        else:
            form = PlannerForm(request.POST)
            return render(request, 'GardenApp/garden_gardenplanner.html',
                          {'form': form})  # pass form to render on gardenplanner.html
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
    harvest = Eval.objects.all()
    context = {'preseason': preseason, 'harvest': harvest}
    return render(request, 'GardenApp/garden_care.html', context)


class SearchView(ListView):
    model = Planner
    template_name = 'GardenApp/garden_search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Planner.objects.filter(Vegetable_Name__contains=query)
            result = postresult
        else:
            result = None
        return result

def vegetable_details(request, pk):
    pk = int(pk)
    vegetable = get_object_or_404(Planner, pk=pk)
    context = {'vegetable': vegetable}
    return render(request, 'GardenApp/garden_details.html', context)
