from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import SharksForm
from .models import Sharks


def SharksApp_home(request):
    return render(request, "SharksApp_home.html")


def Create_Shark(request):
    form = SharksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('SharksApp_newitem')
    else:
        print(form.errors)
        form = SharksForm()
    context = {
        'form': form,
    }
    return render(request, 'SharksApp/templates/SharksApp_newitem.html', context)


def Display_DB(request):
    query_all = Sharks.objects.all()
    content = {
        'query_all': query_all
    }
    return render(request, 'SharksApp/templates/SharksApp_displaydb.html', content)
