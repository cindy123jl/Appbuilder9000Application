from django.shortcuts import render
from .forms import NewTrailForm
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Trails

# This method takes to the homepage of the app.
def home(request):
    return render(request, "HikingFunApp/HikingFunApp_home.html")

# This method creates a form where the user can add a trail to the database.
def new_trail(request):
    # create object of form
    form = NewTrailForm(request.POST or None)
    # check if form data is valid
    if form.is_valid():
        #save is like inserting into database
        form.save()

        return redirect('hiking_home')
    else:
        print(form.errors)
        # form = NewTrailForm()

    context = {'form': form, }
    return render(request, "HikingFunApp/new_trail.html", context)

def see_trails(request):

    trails = Trails.objects.all()
    context = {'trails': trails}
    return render(request, "HikingFunApp/see_trails.html", context)

