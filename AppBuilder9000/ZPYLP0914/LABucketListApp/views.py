from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import DestinationForm
from .models import Destination
from django.core.paginator import Paginator
# Create your views here.

def bucketlist_home(request):
    return render(request, "LABucketListApp/LABucketListApp_home.html")

# Add Destination to database
def bucketlist_create(request):
    form = DestinationForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('BucketList_home')
    context = {'form': form}
    return render(request, 'LABucketListApp/LABucketListApp_create.html', context)


# display all locations from database for index
def bucketlist_index(request):
    form = DestinationForm()
    destinations = Destination.objects.all()
    page = Paginator(destinations, 6)
    page_number = request.GET.get('page')
    page_obj = page.get_page(page_number)
    context = {'form': form, 'destinations': destinations}
    return render(request, 'LABucketListApp/LABucketListApp_index.html', {'page_obj': page_obj}, context)


# displays the details of each destination
def bucketlist_details(request, pk):
    destinations = get_object_or_404(Destination, pk=pk)
    context = {'destinations': destinations}
    return render(request, 'LABucketListApp/LABucketListApp_details.html', context)


# edit the destination
def bucketlist_edit(request, pk):
    destinations = get_object_or_404(Destination, pk=pk)
    form = DestinationForm(data=request.POST or None, instance=destinations)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('BucketList_details', pk)
    context = {'destinations': destinations, 'form': form}
    return render(request, 'LABucketListApp/LABucketListApp_edit.html', context)


# delete function
def bucketlist_delete(request, pk):
    destinations = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        destinations.delete()
        return redirect('BucketList_index')
    else:
        return redirect('BucketList_details', pk)


