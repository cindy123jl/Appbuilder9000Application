from django.shortcuts import render, redirect, get_object_or_404
from .forms import Indoor_PlantForm
from .models import Indoor_Plant
from django.core.paginator import Paginator


# render home page

def home(request):
    return render(request, "PlantApp/PlantApp_home.html")


# Add plant to database
def PlantApp_addPlant(request):
    form = Indoor_PlantForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('PlantApp_home')
    formset = {'form': form}
    return render(request, 'PlantApp/PlantApp_AddPlants.html', formset)


# display added plants from database, pagination for user-friendliness
def index(request):
    form = Indoor_PlantForm()
    plants = Indoor_Plant.objects.all()
    formset = {'form': form, 'plants': plants}
    page = Paginator(plants, 6)
    page_number = request.GET.get('page')
    page_obj = page.get_page(page_number)
    print(plants)
    return render(request, "PlantApp/PlantApp_index.html", {'page_obj': page_obj}, formset)


# Get plant details or 404 error
def details(request, pk):
    plant = get_object_or_404(Indoor_Plant, pk=pk)
    get_details = {'plant': plant}
    print(get_details)
    return render(request, "PlantApp/PlantApp_details.html", get_details)
