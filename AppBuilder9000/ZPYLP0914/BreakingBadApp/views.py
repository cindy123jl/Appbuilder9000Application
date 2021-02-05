from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Episode
from .forms import EpisodeForm


def breakingbad_home(request):
    return render(request, "BreakingBadApp/BreakingBadApp_home.html", )


def breakingbad_addepisode(request):
    form = EpisodeForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('BreakingBadHome')
    context = {'form': form}
    return render(request, "BreakingBadApp/BreakingBadApp_addepisode.html", context)


def breakingbad_savedepisodes(request):
    episodes = Episode.Episodes.all()
    paginator = Paginator(episodes, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "BreakingBadApp/BreakingBadApp_index.html", {'page_obj': page_obj})


def breakingbad_details(request, pk):
    pk = int(pk)
    episode = get_object_or_404(Episode, pk=pk)
    details = {'episode': episode}
    return render(request, 'BreakingBadApp/BreakingBadApp_details.html', details)


def breakingbad_edit(request, pk):
    pk = int(pk)
    episode = get_object_or_404(Episode, pk=pk)
    form = EpisodeForm(data=request.POST or None, instance=episode)
    if request.method == 'POST':
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('BreakingBadSavedEpisodes')
        else:
            print(form.errors)
    else:
        return render(request, 'BreakingBadApp/BreakingBadApp_edit.html', {'form': form})


def breakingbad_delete(request, pk):
    episode = get_object_or_404(Episode, pk=pk)
    episode.delete()
    return redirect('BreakingBadSavedEpisodes')
