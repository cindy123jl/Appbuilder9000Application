from django.shortcuts import render
from .forms import wordform, etymologyform

def WordNerd_home(request):
    return render(request, 'wordnerd/WordNerd_home.html')

def WordNerd_createword(request):
    wform = wordform()
    if request.method == 'POST':
        print(request.POST)
        wform = wordform(request.POST)
        if wform.is_valid():
            wform.save()

    eform = etymologyform()
    if request.method == 'POST':
        print(request.POST)
        eform = etymologyform(request.POST)
        if eform.is_valid():
            eform.save()

    context = {
        'wform': wform,
        'eform': eform,
    }
    return render(request, 'wordnerd/WordNerd_createword.html', context)

