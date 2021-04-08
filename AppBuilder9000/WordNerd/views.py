from django.shortcuts import render


def WordNerd_home(request):
    return render(request, 'wordnerd/WordNerd_home.html')