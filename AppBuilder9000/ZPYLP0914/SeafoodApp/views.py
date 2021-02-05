from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Seafood
from .forms import SeafoodForm


def seafood_home(request):
    return render(request, "SeafoodApp/SeafoodApp_home.html")


def seafoodadd(request):
    addseafoodform = SeafoodForm(data=request.POST or None)
    if request.method == 'POST' and addseafoodform.is_valid() and 'Add_Seafood' in request.POST:
        addseafoodform.save()
        return redirect('seafoodadd')
    content = {'addseafoodform': addseafoodform}
    print(Seafood.wild_caught)
    return render(request, 'SeafoodApp/SeafoodApp_add.html', content)


def seafoodlookup(request):
    all_entries = Seafood.SeafoodIndex.all()
    content = {'all_entries': all_entries}
    return render(request, 'SeafoodApp/SeafoodApp_lookup.html', content)


def seafoodsearch(request):
    if request.method == 'GET':
        search = request.GET.get('searchbox')
        post = Seafood.SeafoodIndex.all().filter(name__icontains=search)
        print(post)
        content = {'post': post}
        return render(request, 'SeafoodApp/SeafoodApp_search.html', content)
    else:
        return render(request, "SeafoodApp/SeafoodApp_home.html")


def details(request, pk):
    return render(request, 'SeafoodApp/SeafoodApp_details.html', {'seafood': Seafood.SeafoodIndex.get(pk=pk)})

