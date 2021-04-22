from django.shortcuts import render

# Create your views here.
def Theater_home(request):
    return render(request, 'Theaters_and_Features/Theaters_and_Features_home.html')


