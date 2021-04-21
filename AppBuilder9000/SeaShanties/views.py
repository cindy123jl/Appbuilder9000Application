from django.shortcuts import render, redirect
from .forms import ShantiesForm

# Create your views here.


def shantieshome(request):
    context = {}
    return render(request, 'SeaShanties/shanties_home.html', context)


def addsong(request):
    context = {}
    return render(request, 'SeaShanties/shanties_add.html', context)


def shantiesadd(request):
    if request.method == 'POST':
        form = ShantiesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shanties_add')
        else:
            form = ShantiesForm(request.POST)
            return render(request, 'ShantiesApp/shanties_add.html',
                          {'form': form})  # pass form to render on gardenplanner.html
    else:
        form = ShantiesForm(None)
        return render(request, 'SeaShanties/shanties_add.html', {'form': form})
