from django.shortcuts import render, redirect
from .forms import ConcertForm, OrchestraForm, PieceForm, ConductorForm
from .models import Concert, Piece, Conductor, Orchestra
# Create your views here.


def home(request):
    return render(request, 'UpcomingConcertsApp/home.html')


def add_event(request):
    concert_form = ConcertForm(prefix='concert')
    orchestra_form = OrchestraForm(prefix='orchestra')
    piece_form = PieceForm(prefix='piece')
    conductor_form = ConductorForm(prefix='conductor')

    if request.method == 'POST':
        if 'Save_Event' in request.POST:
            concert_form = ConcertForm(request.POST, prefix='concert')
            if concert_form.is_valid():
                concert_form.save()
                return redirect('add_event')
        elif 'Save_Orchestra' in request.POST:
            orchestra_form = OrchestraForm(request.POST, prefix='orchestra')
            if orchestra_form.is_valid():
                orchestra_form.save()
                return redirect('add_event')
        elif 'Save_Piece' in request.POST:
            piece_form = PieceForm(request.POST, prefix='piece')
            if piece_form.is_valid():
                piece_form.save()
                return redirect('add_event')
        elif 'Save_Conductor' in request.POST:
            conductor_form = ConductorForm(request.POST, prefix='conductor')
            if conductor_form.is_valid():
                conductor_form.save()
                return redirect('add_event')

    content = {'concert_form': concert_form, 'orchestra_form': orchestra_form,
               'conductor_form': conductor_form, 'piece_form': piece_form}
    return render(request, 'UpcomingConcertsApp/add_event.html', content)


def display_items(request):
    all_events = Concert.concerts.all()
    all_event_pieces = Concert.pieces.through.objects.all()
    all_orchestras = Orchestra.orchestras.all()
    all_pieces = Piece.pieces.all()
    all_conductors = Conductor.conductors.all()
    context = {'all_events': all_events, 'all_orchestras': all_orchestras,
               'all_pieces': all_pieces, 'all_conductors': all_conductors,
               'all_event_pieces': all_event_pieces}

    return render(request, 'UpcomingConcertsApp/display_items.html', context)
