from django.shortcuts import render
from .forms import wordform
from .models import word
from django.http import HttpResponse

def WordNerd_home(request):
    return render(request, 'wordnerd/WordNerd_home.html')

def WordNerd_createword(request):
    wordForm = wordform()
    if request.method == 'POST':
        print(request.POST)
        wordForm = wordform(request.POST)
        if wordForm.is_valid():
            wordForm.save()
    context = {'wordForm': wordForm}
    return render(request, 'wordnerd/WordNerd_createword.html', context)

def WordNerd_viewdata(request):
    allWords = word.objects.all
    context = {
        'allWords': allWords
    }
    return render(request, "wordnerd/WordNerd_viewdata.html", context)
#uses primary key as a filter tag for selecting the chosen word
def WordNerd_worddetails(request, pk):
    pk = int(pk)
    word_get = word.objects.filter(pk=pk)
    context = {'word_get': word_get}
    return render(request, "wordnerd/WordNerd_worddetails.html", context)



