from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from .forms import BudgetForm, BudgetInfo
# Create your views here.


def home(request):
    return render(request, 'BudgetingApp/BudgetingApp_home.html')

def login(request):
    return render(request, 'BudgetingApp/BudgetingApp_login.html')


def create_budget(request):

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request
        form = BudgetForm(request.POST)
        form.save()  # will validate form and save

    form = BudgetForm()

    budget = BudgetInfo.objects.all()

    context = {
        'form': form
    }

    return render(request, 'BudgetingApp/BudgetingApp_budget.html', context)



