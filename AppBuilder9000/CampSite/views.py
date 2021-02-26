from django.shortcuts import render, redirect, get_object_or_404
from .forms import CampsiteForm
from .models import Campsite


def campsite_home(request):
    return render(request, 'CampSite/CampSite_home.html')


def add_campsite(request):
    form = CampsiteForm(data=request.POST or None)
    if request.method == 'POST':
        print('method is POST')
        if form.is_valid():
            print('form is valid')
            form.save()
            return redirect('home')
    content = {'form': form}
    return render(request, 'CampSite/add_campsite.html', content)

def browse(request):
    campsite = Campsite.Campsites.all()
    content = {'campsite': campsite}
    return render(request, 'CampSite/browse_campsites.html', content)

