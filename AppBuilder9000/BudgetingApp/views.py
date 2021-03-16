from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'BudgetingApp/BudgetingApp_home.html')

def login(request):
    return render(request, 'BudgetingApp/BudgetingApp_login.html')


