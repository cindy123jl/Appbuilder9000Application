from django.shortcuts import render


def MusicApp_home(request):

    return render(request, 'MusicApp/MusicApp_home.html')
