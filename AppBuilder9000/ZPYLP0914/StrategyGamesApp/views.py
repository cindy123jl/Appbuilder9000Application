from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpResponse
from .models import StrategyGame
from .forms import StrategyGamesForm
from django.http import Http404


# Create your views here.

def index(request):
    return render(request, "StrategyGamesApp/home.html")





def Display_Games(request):
    games = StrategyGame.objects.all()
    content = {'games':games,}
    return render(request, 'StrategyGamesApp/StrategyGamesAppDatabaseDisplay.html', content)


def game_create(request):
    AddGameForm = StrategyGamesForm(data=request.POST or None)
    if request.method == 'POST' and  AddGameForm.is_valid() and 'Add_Game' in request.POST:
        AddGameForm.save()
        return redirect('add game')
    content = {'addgameform': AddGameForm}
    return render(request, "StrategyGamesApp/StrategyGameAppAdd.html", content)

def details(request, pk):
    try:
        data = StrategyGame.objects.get(id = pk)
    except StrategyGame.DoesNotExist:
        raise Http404('Data does not exist')
    return render(request, 'StrategyGamesApp/details.html', {'StrategyGame': StrategyGame})
