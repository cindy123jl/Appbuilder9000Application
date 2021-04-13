from django.shortcuts import render

# Create your views here.


def shantieshome(request):
    context = {}
    return render(request, 'SeaShanties/shanties_home.html', context)
