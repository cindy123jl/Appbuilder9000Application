from django.shortcuts import render, redirect
from .forms import CampsiteForm


def campsite_home(request):
    return render(request, 'CampSite/CampSite_home.html')


def add_campsite(request):
    form = CampsiteForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    content = {'form': form}
    return render(request, 'CampSite/add_campsite.html', content)
