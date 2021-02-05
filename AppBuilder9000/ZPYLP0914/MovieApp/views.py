from django.shortcuts import render, redirect, get_object_or_404
import requests
from .models import User, Movie
from .forms import CreateProfile
import json
# Create your views here.
#API KEY = https://api.themoviedb.org/3/movie/550?api_key=
#
auth = {'user-key': '3208289ff2576160ceb2d701742981eb'}
auth1 = {'user-key': '20e33147579d00d283d48d69dad250afb773701a'}
def home(request):
    return render(request, 'MovieApp/movieapp_home.html')


def create_profile(request):
    form = CreateProfile(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('MovieAppHome')
    context = {'form': form}
    return render(request, 'MovieApp/create_profile.html', context)


def movieapp_index(request):
    user = User.Users.all()
    context = {'user': user}
    return render(request, 'MovieApp/movieapp_index.html', context)


def movieapp_details(request, pk):
    user = get_object_or_404(User, pk=pk)
    context = {'user': user}
    return render(request, 'MovieApp/movieapp_details.html', context)




def movieapp_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('movieapp_index')
    context = {'user': user}
    return render(request, 'MovieApp/movieapp_delete.html', context)


def movieapp_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = CreateProfile(request.POST or None, request.FILES or None, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            user.save()
            return redirect('movieapp_index')
    context = {'user': user, 'pk': pk, 'form': form}
    return render(request, 'MovieApp/movieapp_edit.html', context)


def movieapp_api(request):
    movie = request.POST.get('userMovie')
    response = requests.get('https://api.themoviedb.org/3/search/movie?api_key=3208289ff2576160ceb2d701742981eb&query={}'.format(movie))
    obj = response.json()["results"][0]
    #searching by movie title to get title, release date, and summary
    title = obj["title"]
    release_date = obj["release_date"]
    overview = obj["overview"]
    context = {'overview': overview, 'title': title, 'release_date': release_date}
    return render(request, 'MovieApp/movieapp_api.html', context)