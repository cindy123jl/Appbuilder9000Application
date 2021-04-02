from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipeForm


def home(request):
    return render(request, 'WorldRecipes/WR_home.html')


def create_recipes(request):
    form = RecipeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('WR_create_recipes')
    context = {'form': form}
    return render(request, 'WorldRecipes/WR_create_recipes.html', context)

