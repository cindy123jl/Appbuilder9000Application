from django.shortcuts import render, redirect
from .forms import GuitarForm


# Create your views here.
def home(request):
    return render(request, 'GuitarReviewsApp/GuitarReviewsApp_home.html')


def create(request):
    form = GuitarForm(request.POST or None)
    if request.method == "POST":
        # check if form is valid
        # if so, save
        if form.is_valid():
            form.save()
            return redirect("GuitarReviews_create")

    context = {'form': form}
    return render(request, "GuitarReviewsApp/GuitarReviewsApp_create.html", context)
