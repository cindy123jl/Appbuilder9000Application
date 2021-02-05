from django.shortcuts import render, redirect, get_object_or_404
from .forms import CocktailForm
from .models import Cocktail

from django.core.paginator import Paginator

import requests
import json



# Render home page
def CocktailsApp_home(request):
    return render(request, 'CocktailsApp/CocktailsApp_home.html')


# Add Cocktail to database
def create(request):
    if request.method == 'POST':
        form = CocktailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('CocktailsApp_index')
    else:
        form = CocktailForm()
    context = {'form': form}
    return render(request, 'CocktailsApp/CocktailsApp_create.html', context)

# Render Cocktails index page
def CocktailsApp_index(request):
    return render(request, 'CocktailsApp/CocktailsApp_index.html')

# Display added cocktails from db with pagination
def index(request):
    form = CocktailForm()
    cocktails = Cocktail.objects.all()
    page = Paginator(cocktails, 3)
    page_number = request.GET.get('page')
    page_obj = page.get_page(page_number)
    context = {'form': form, 'cocktails': cocktails}
    return render(request, 'CocktailsApp/CocktailsApp_index.html', {'page_obj': page_obj}, context)

# Display details (ingredients) of a single cocktail from within db
def details(request, pk):
    return render(request, 'CocktailsApp/CocktailsApp_details.html', {'cocktail': Cocktail.objects.get(pk=pk)})

# Render Cocktails edit page
def edit(request, pk):
    cocktail = get_object_or_404(Cocktail, pk=pk)
    form = CocktailForm(data=request.POST or None, instance=cocktail)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('CocktailsApp_details', pk)
    context = {'cocktail': cocktail, 'form': form}
    return render(request, 'CocktailsApp/CocktailsApp_edit.html', context)

# Delete a cocktail from the db
def delete(request, pk):
    cocktail = get_object_or_404(Cocktail, pk=pk)
    if request.method == 'POST':
        cocktail.delete()
        return redirect('CocktailsApp_index')
    else:
        return redirect('CocktailsApp_details', pk)

# render API page and print drink instructions to terminal when user inputs a cocktail name
# def CocktailsApp_api(request):
#     cocktail = {}
#     drink_instructions = []
#     if 'cocktail_name' in request.GET:
#         cocktail_name = request.GET['cocktail_name']
#         parameters = {"s": cocktail_name}
#         response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?s=', params=parameters)
#         cocktail = response.json()['drinks']
#         for i in cocktail:
#             instructions = i['strInstructions']
#             drink_instructions.append(instructions)
#             print("\nThe instructions to make a {}:\n".format(cocktail_name) + instructions + "\n")
#
#     return render(request, 'CocktailsApp/CocktailsApp_api.html', {'drink_instructions': drink_instructions})


def CocktailsApp_api(request):
    cocktail = {'drinks': 'yes'}
    if 'cocktail_name' in request.GET:
        cocktail_name = request.GET['cocktail_name']
        print(cocktail)
        if cocktail_name == "":
            print("Not a valid cocktail name in the API.")
            cocktail = {'drinks': None}
            print(cocktail)
        else:
            parameters = {"s": cocktail_name}
            response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?s=', params=parameters)
            cocktail = response.json()
            print(cocktail)
        # print(cocktail['drinks'])
        # print(type(cocktail['drinks']))
    return render(request, 'CocktailsApp/CocktailsApp_api.html', {'cocktail': cocktail})









