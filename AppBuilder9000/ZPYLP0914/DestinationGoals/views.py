from django.shortcuts import render, redirect, get_object_or_404
from .models import Destination
from .forms import DestinationForm
# Render home page
def DestinationGoals_home(request):
    return render(request, 'DestinationGoals/DestinationGoals_home.html')

# Add Destination to database
def DestinationGoals_create(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Destination_index')
    else:
        form = DestinationForm()
    context = {'form': form}
    return render(request, 'DestinationGoals/DestinationGoals_create.html', context)

# Lists all the items in the database
def Destination_index(request):

    allDestinations = Destination.objects.all()
    return render(request, 'DestinationGoals/Destination_index.html', {'all': allDestinations})

# Takes you to the details page for the item selected
def DestinationGoals_details(request,pk): # passes the id attribute from the urls
    pk = int(pk)
    context = {}
    context ["data"] = Destination.objects.get (pk=pk)

    return render(request, 'DestinationGoals/DestinationGoals_details.html', context)

def DestinationGoals_edit(request, pk):
    context = {}

    destination_data = get_object_or_404(Destination, pk=pk)
    form = DestinationForm(data=request.POST or None, instance=destination_data)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Destination_index')
        else:
            print(form.errors)
    else:
        context["form"] = form
        return render(request, 'DestinationGoals/DestinationGoals_edit.html',context)

def DestinationGoals_delete(request,pk):
    pk = int(pk)
    item = get_object_or_404(Destination, pk=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('Destination_index')


    context = {'item':item}
    return render(request, 'DestinationGoals/DestinationGoals_confirmDelete.html', context)


def confirm_delete(request):
    if request.method == "Post":
        form = DestinationForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('Destination_index')
    else:
        return redirect('Destination_index')

