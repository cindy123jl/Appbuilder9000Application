from django.shortcuts import render

# Create your views here.
def home(request):
    print("Home method")
    return render(request, 'GuitarReviewsApp/GuitarReviewsApp_home.html')

