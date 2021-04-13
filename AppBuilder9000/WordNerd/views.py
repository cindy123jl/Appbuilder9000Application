from django.shortcuts import render
from .forms import wordform
from .models import word

def WordNerd_home(request):
    return render(request, 'wordnerd/WordNerd_home.html')

def WordNerd_createword(request):
    wform = wordform()
    if request.method == 'POST':
        print(request.POST)
        wform = wordform(request.POST)
        if wform.is_valid():
            wform.save()
    context = {'wform': wform}
    return render(request, 'wordnerd/WordNerd_createword.html', context)

def WordNerd_viewdata(request):
    wAll = word.objects.all
    context = {
        'wAll': wAll
    }
    return render(request, "wordnerd/WordNerd_viewdata.html", context)

