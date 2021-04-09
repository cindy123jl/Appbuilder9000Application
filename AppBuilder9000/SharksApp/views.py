from django.shortcuts import render
from django.http import HttpResponse

def SharksApp_home(request):
    return render(request, "SharksApp_home.html")

