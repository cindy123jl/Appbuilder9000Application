from django.shortcuts import render


def MyThai_home(request):
    return render(request, 'MyThai/MyThai_home.html')
