from django.shortcuts import render, redirect, get_object_or_404
from .forms import CampsiteForm
from .models import Campsite
from bs4 import BeautifulSoup
import requests



def campsite_home(request):
    return render(request, 'CampSite/CampSite_home.html')

# Add a new campsite to the dB
def add_campsite(request):
    form = CampsiteForm(request.POST or None, request.FILES)
    if request.method == 'POST':
        print('method is POST')
        if form.is_valid():
            print('form is valid')
            form.save()
            return redirect('browse')
    context = {'form': form}
    return render(request, 'CampSite/add_campsite.html', context)

# Show list of all campsites in dB
def browse(request):
    campsite = Campsite.Campsites.all()
    context = {'campsite': campsite}
    return render(request, 'CampSite/browse_campsites.html', context)

# Get campsite details from browse page
def campsite_details(request, campsite_id):
    campsite = get_object_or_404(Campsite, pk=campsite_id)
    context = {'campsite': campsite}
    return render(request, 'Campsite/campsite_details.html', context)

# Edit campsite from details page
def edit_campsite(request, campsite_id):
    # Get campsite object from dB via id
    campsite = get_object_or_404(Campsite, pk=campsite_id)
    if request.method == 'POST':
        # Display info for campsite instance as form
        form = CampsiteForm(data=request.POST, instance=campsite)
        if form.is_valid():
            # Save changes if form is valid and redirect back to details page (w/ updates)
            form.save()
            return redirect('campsite_details', campsite.id)
    else:
        form = CampsiteForm(instance=campsite)
    context = {'form': form}
    return render(request, 'CampSite/edit_campsite.html', context)


def delete_campsite(request, campsite_id):
    campsite = get_object_or_404(Campsite, pk=campsite_id)
    campsite.delete()
    return redirect('browse')

def bs_scrape(request):
    # Get forest service page with list of campsites, assign to variable
    page = requests.get("https://www.fs.usda.gov/activity/mthood/recreation/camping-cabins/?recid=52770&actid=29")
    print(page.status_code)
    # Use Beautiful Soup to parse html
    soup = BeautifulSoup(page.content, 'html.parser')

    print(soup.prettify)
    return render(request, 'CampSite_nationalForest')




