from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def quantumapp_home(request):
    return render(request, 'quantumapp/quantum_home.html')
