from django.shortcuts import render
from .forms import NewTrailForm

# Create your views here.
def home(request):
    return render(request, "HikingFunApp/HikingFunApp_home.html")


def new_trail(request):
    # creaste object of form
    form = NewTrailForm(request.POST or None)
    # check if form data is valid
    if form.is_valid():
        #save the form data to model
        form.save()

    context = {'form': form}
    return render(request, "HikingFunApp/new_trail.html", context)


