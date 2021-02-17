from django.shortcuts import render
from .forms import NewTrailForm
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, "HikingFunApp/HikingFunApp_home.html")


def new_trail(request):
    # create object of form
    form = NewTrailForm(request.POST or None)
    # check if form data is valid
    if form.is_valid():
        #save the form data to model
        form.save()
        return redirect('hiking_home') # is this the webaddress home/ or the name= home
    else:
        print(form.errors)
        form = NewTrailForm()

    context = {'form': form, }
    return render(request, "HikingFunApp/new_trail.html", context)


