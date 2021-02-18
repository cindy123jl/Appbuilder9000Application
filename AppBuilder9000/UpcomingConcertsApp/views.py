from django.shortcuts import render
from .forms import ConcertForm, OrchestraForm, PieceForm, ConductorForm
from .models import Concert, Orchestra, Piece, Conductor

# Create your views here.


def home(request):
    return render(request, 'UpcomingConcertsApp\\home.html')


def add_event(request):
    concert_form = ConcertForm(request.POST or None)
    if request.method == 'POST':
        if concert_form.is_valid():
            concert_form.save()

    orchestra_form = OrchestraForm(request.POST or None)
    if request.method == 'POST':
        if orchestra_form.is_valid():
            orchestra_form.save()

    piece_form = PieceForm(request.POST or None)
    if request.method == 'POST':
        if piece_form.is_valid():
            piece_form.save()

    conductor_form = ConductorForm(request.POST or None)
    if request.method == 'POST':
        if conductor_form.is_valid():
            conductor_form.save()

    content = {'concert_form': concert_form, 'orchestra_form': orchestra_form,
               'conductor_form': conductor_form, 'piece_form': piece_form}
    return render(request, 'UpcomingConcertsApp/add_event.html', content)
