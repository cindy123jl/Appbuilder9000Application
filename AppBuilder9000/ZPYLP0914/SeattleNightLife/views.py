from django.shortcuts import render, redirect, get_object_or_404
from .models import Venue
from .forms import VenueForm

# Create your views here.


def nightlife_home(request):
    return render(request, 'SeattleNightLife/SeattleNightLife_home.html')

def nightlife_create(request):
    form = VenueForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('SeattleNightLife_index')
    content = {'form': form}
    return render(request, 'SeattleNightLife/SeattleNightLife_create.html',content)


def nightlife_index(request):
    #call all data from table Venue, store into variable allVenues
    allVenues = Venue.objects.all()
    return render(request, 'SeattleNightLife/SeattleNightLife_index.html', {'all': allVenues})
    #sends that data to the index webpage where it will be unpacked with html/css/python code (template language)

def nightlife_details(request,pk): # passes the id attribute from the urls
    pk = int(pk)
    context = {}
    # creates a dictionary for the initial data with field names as key
    context ["data"] = Venue.objects.get (pk=pk)

    return render(request, 'SeattleNightLife/SeattleNightLife_details.html', context)

def nightlife_edit(request, pk):
    context = {}
    # creates a dictionary for the initial data with field names as key
    venue_data = get_object_or_404(Venue, pk=pk)
    #retrieves the data contained in the row pertaining to the primary key for the selected venue
    form = VenueForm(data=request.POST or None, instance=venue_data)
    #passes the data obtained from the table into the form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('SeattleNightLife_index')
            # saves the updates to database, closes the edit.html by redirecting to the index.html page
        else:
            print(form.errors)
    else:
        context["form"] = form
        return render(request, 'SeattleNightLife/SeattleNightLife_edit.html',context)

def nightlife_delete(request,pk):
    pk = int(pk)
    item = get_object_or_404(Venue, pk=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('SeattleNightLife_index')
        #this is the second step of the definition, after the confirm_delete definition has run
        #and user confirm deletion by clicking the Yes button

    context = {'item':item}
    return render(request, 'SeattleNightLife/SeattleNightLife_confirmDelete.html', context)
    # that's actually the first step of the function - getting a confirmation from the user
    #by calling the confirmDelete webpage which will trigger the confirm_delete definition

def confirm_delete(request):
    #this function is triggered by rendering the confirm_delete page in the delete definition.
    if request.method == "Post":
        form = VenueForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('SeattleNightLife_index')
    else:
        return redirect('SeattleNightLife_index')

