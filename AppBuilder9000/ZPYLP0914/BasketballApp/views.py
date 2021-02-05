from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreatePlayerForm
from .models import CreatePlayer
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    return render(request, 'BasketballApp/BasketballApp_home.html')

def add_player(request):
    form = CreatePlayerForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('BasketballApp_home')
    else:
        print(form.errors)
        form = CreatePlayerForm()
    context = {'form': form}
    return render(request, 'BasketballApp/add_player.html', context)

def index(request):
    form = CreatePlayerForm()
    players = CreatePlayer.object.all()
    page = Paginator(players, 5)
    page_number = request.GET.get('page')
    page_obj = page.get_page(page_number)
    context = {'form': form, 'players': players}
    return render(request, 'BasketballApp/BasketballApp_index.html', {'page_obj': page_obj}, context)

#Gets player details or returns error 404
def BasketballApp_details(request, pk):
    player = get_object_or_404(CreatePlayer, pk=pk)
    detail = {'player': player}
    return render(request, 'BasketballApp/BasketballApp_details.html', detail)