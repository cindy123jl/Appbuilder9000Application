from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('hello')

def gardenplanner(request):
   return HttpResponse('hello')

def contact(request):
   return HttpResponse('hello from contact')