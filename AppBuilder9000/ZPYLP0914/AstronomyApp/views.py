

# Create your views here.
from django.http import HttpResponse

from .forms import PlanetForm
from django.shortcuts import render, redirect
from .models import Planet


def home(request):
    return render(request, 'AstronomyApp/AstronomyApp_home.html')


def manage_planets(request):
    form = PlanetForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('AstronomyApp')
    formset = {'form': form}
    return render(request, 'AstronomyApp/AstronomyApp_AddPlanet.html', formset)


def planet_index(request):
    planets = Planet.objects.all() # this will fetch all planets from database
    print(planets)
    context = {'planets': planets}
    return render(request, 'AstronomyApp/AstronomyApp_index.html', context)


def details(request, pk):
    return render(request, 'AstronomyApp/AstronomyApp_details.html', {
        'planet': Planet.objects.get(pk=pk)
    })

