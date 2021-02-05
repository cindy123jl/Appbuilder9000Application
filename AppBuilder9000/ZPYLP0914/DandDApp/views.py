from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import CreateCharacterForm
from .models import CreateCharacter
from django.views.generic.list import ListView
from django.core.paginator import Paginator
import requests
from bs4 import BeautifulSoup


# Home Page
def d_and_d_home(request):
    return render(request, 'DandDApp/DandD_home.html')


# ADD- adds character to DB
def add_character(request):
    form = CreateCharacterForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('d_and_d_home')
    else:
        print(form.errors)
        form = CreateCharacterForm()
    context = {'form': form}
    return render(request, 'DandDApp/Add_Character.html', context)


# Index--Shows all entries in DB
def d_and_d_index(request):
    form = CreateCharacterForm()
    characters = CreateCharacter.object.all()
    paginator = Paginator(characters, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'form': form, 'characters': characters}
    return render(request, 'DandDApp/DandD_index.html', {'page_obj': page_obj}, context)


# Details-- retrieves details on any Db entry
def d_and_d_details(request, pk):
    character = get_object_or_404(CreateCharacter, pk=pk)
    context = {'character': character}
    return render(request, 'DandDApp/DandD_Details.html', context)


# Edit-- update character in DB.
def d_and_d_edit(request, pk):
    character = get_object_or_404(CreateCharacter, pk=pk)
    # HTTP method POST-- finds the form that was submitted by a user
    if request.method == 'POST':
        form = CreateCharacterForm(request.POST, instance=character)
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('d_and_d_index')
        else:
            print(form.errors)
    else:
        form = CreateCharacterForm(instance=character)
        context = {'form': form, }
    return render(request, 'DandDApp/DandD_edit.html', context)


# Delete -- delete character from DB
def d_and_d_delete(request, pk):
    character = get_object_or_404(CreateCharacter, pk=pk)
    if request.method == 'POST':
        character.delete()
        return redirect('d_and_d_index')
    context = {'character': character, }
    return render(request, 'DandDApp/DandD_delete.html', context)


# Article -- uses beautful soup to parse page for article summaries and authors.
def d_and_d_article(request):
    page = requests.get("https://dnd.wizards.com/articles")
    soup = BeautifulSoup(page.content, 'html.parser')
    articles = soup.find_all('div', class_='content')
    articleList = []
    for item in articles:
        Author = item.find(class_='author')
        if Author is not None:
            # prints authors name to console
            print(Author.find('a').text)
            # .text is calling on the beautiful soup property to pull text
            AuthorRefined = Author.find('a').text
            Summary = item.find(class_='summary').text
            artsum = {"Author": AuthorRefined, "Summary": Summary}

            articleList.append(artsum)
    # prints article author and summary to console 
    print(articleList)

    return render(request, 'DandDApp/DandD_soup.html', {'articleList': articleList})
