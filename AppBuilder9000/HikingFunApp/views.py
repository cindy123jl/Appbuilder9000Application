from django.shortcuts import render, get_object_or_404
from .forms import NewTrailForm
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Trails

# This method takes to the homepage of the app.
def home(request):
    trails = Trails.objects.all()
    context = {'trails': trails}
    return render(request, "HikingFunApp/HikingFunApp_home.html", context)

# This method creates a form where the user can add a trail to the database.
def new_trail(request):
    # create object of form
    form = NewTrailForm(request.POST or None)
    # check if form data is valid
    if form.is_valid():
        #save is like inserting into database
        form.save()

        return redirect('added_trails')
    else:
        print(form.errors)
        # form = NewTrailForm()
    trails = Trails.objects.all()

    context = {'form': form, 'trails': trails, }
    return render(request, "HikingFunApp/new_trail.html", context)

# This method helps the webpage to show all the trails in the database.
def see_trails(request):
    trails = Trails.objects.all()
    context = {'trails': trails}
    return render(request, "HikingFunApp/see_trails.html", context)

# This method renders to html page that shows a  message that you successfully added a trial.
def added_trails(request):
    trails = Trails.objects.all()
    context = {'trails': trails}
    return render(request, "HikingFunApp/added_trails.html", context)

# This method shows the details of the trail link that is clicked from the side bar
def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Trails, pk=pk)
    form = NewTrailForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('see_trails')
        else:
            print(form.errors)
    else:
        return render(request, "HikingFunApp/details.html", {'form': form, 'item': item})

# This method gives the trails info  to webpage that displays the sidebar.
def side_bar(request):
    trails = Trails.objects.all()
    context = {'trails': trails}
    return render(request, "HikingFunApp/side_bar.html", context)



# If the item with this pk doesn't exist, throw error, if it exists, and method of submitting is POST
# delete and go back to trails list. Else go to confirm deletion from the user.
def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Trails, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('see_trails')
    context = {"item": item, }
    return render(request, "HikingFunApp/confirm_delete.html", context)


def confirmed(request):
    if request.method == 'POST':
        # creates form instance and binds data to it
        form = NewTrailForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('hiking_home')
    else:
        return redirect("see_trails")
