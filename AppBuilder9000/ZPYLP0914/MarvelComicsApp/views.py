from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateCharacter, SaveFavorite
from .models import Character
from django.core.paginator import Paginator
#For the Marvel Comics API
import requests
from datetime import datetime
from hashlib import md5
import random
import re
#For Beautiful Soup
from bs4 import BeautifulSoup


def search_view(request):
    #grabbing the info that was entered into the search bar and putting it into the variable 'data'
    data = request.GET.get('search')
    #passing the variable 'data' to the results_view
    return redirect('MarvelComicsAppResults', data)

def home(request):
    #using the django render function to show the MarvelComicsApp_home.html file
    return render(request, 'MarvelComicsApp/MarvelComicsApp_home.html')

def character_create_view(request):
    form = CreateCharacter(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('MarvelComicsAppHome')
    return render(request, "MarvelComicsApp/MarvelComicsApp_character_create.html", {'form': form})

def character_index_view(request):
    characters_list = Character.object.all()
    paginator = Paginator(characters_list, 5)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        characters = paginator.page(page)
    except(EmptyPage, InvalidPage):
        characters = paginator.page(paginator.num_pages)
    return render(request, 'MarvelComicsApp/MarvelComicsApp_character_index.html', {'characters': characters})

def character_detail_view(request, pk):
    characters = get_object_or_404(Character, pk=pk)
    return render(request, 'MarvelComicsApp/MarvelComicsApp_character_detail.html', {'characters': characters})

def character_edit_view(request, pk):
    characters = get_object_or_404(Character, pk=pk)
    if request.method == 'POST':
        form = CreateCharacter(request.POST, instance=characters)
        if form.is_valid():
            characters.save()
            return redirect('MarvelComicsAppCharacterDetail', pk=characters.pk)
    else:
        form = CreateCharacter(instance=characters)
    return render(request, 'MarvelComicsApp/MarvelComicsApp_character_edit.html', {'form': form})

def character_delete_view(request, pk):
    characters = get_object_or_404(Character, pk=pk)
    if request.method == 'POST':
        characters.delete()
        return redirect('MarvelComicsAppCharacterIndex')
    return render(request, 'MarvelComicsApp/MarvelComicsApp_character_delete.html', {'characters':characters})



#varibales used for the hash_params function, results_view, and random_view
timestamp = datetime.now().strftime('%y-%m-%d%H:%M:%S')
pub_key = 'd14caeb1fb2188a04c30c89c3ed44406'
priv_key = '275f19d292e0b0bd391fe9e865183083531a37b5'

#will not be displayed as a view but is needed for the results and random_view
def hash_params():
    hash_md5 = md5()
    hash_md5.update(f'{timestamp}{priv_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()
    return hashed_params

def results_view(request, data):
    params = {'nameStartsWith': data,
              'limit': 5,
              'ts': timestamp,
              'apikey': pub_key,
              'hash': hash_params(),
              }
    res = requests.get('https://gateway.marvel.com:443/v1/public/characters', params=params)
    results = res.json()
    characters = results['data']['results']
    attributiontext = results['attributionText']
    overview = re.compile('.*marvel.com\/characters\/.*')
    heros_info = character_search(characters, overview, attributiontext)
    save_favorite_view(request)

    return render(request, 'MarvelComicsApp/MarvelComicsApp_search_results.html', {'heros_info': heros_info})

def random_view(request):
    params = {'limit': 1,
              'offset': random.randrange(1, 1500),
              'ts': timestamp,
              'apikey': pub_key,
              'hash': hash_params(),
              }
    res = requests.get('https://gateway.marvel.com:443/v1/public/characters', params=params)
    results = res.json()
    characters = results['data']['results']
    overview = re.compile('.*marvel.com\/characters\/.*')
    attributiontext = results['attributionText']
    heros_info = character_search(characters, overview, attributiontext)
    save_favorite_view(request)

    return render(request, 'MarvelComicsApp/MarvelComicsApp_search_random.html', {'heros_info': heros_info})

def character_search(characters, overview, attributiontext):
    hero_info = []
    for character in characters:
        images = character['thumbnail']
        characters_urls = character['urls']
        links = ''
        for character_url in characters_urls:
            hero_url = character_url['url']
            if overview.match(hero_url):
                links = hero_url
                break
        characters_info = {'names': character['name'],
                           'descriptions': character['description'],
                           'paths': images['path'],
                           'extensions': images['extension'],
                           'id': character['id'],
                           'hero_link': links,
                           'attriText': attributiontext,
                           }
        hero_info.append(characters_info)
    return hero_info

def save_favorite_view(request):
    form = SaveFavorite(request.POST)
    if form.is_valid():
        form.save()

def comic_news_view(request):
    page = requests.get('https://www.marvel.com/articles')
    soup = BeautifulSoup(page.content, 'html.parser')
    comic_news_section = soup.find_all(href=re.compile('.*marvel.com\/articles\/comics.*'))
    #scrapping all comics news from the Marvel site. There are only three visible articles on the site at one time
    article_one = comic_news_section[1]
    article_two = comic_news_section[3]
    article_three = comic_news_section[5]
    #scrapping the text from the article summary and putting it into a dictionary

    story_one = {'summary': article_one.get_text(),
                 'link': article_one.get('href')
                 }
    story_two = {'summary': article_two.get_text(),
                 'link': article_two.get('href')
                 }
    story_three = {'summary': article_three.get_text(),
                 'link': article_three.get('href')
                 }
    stories = [story_one, story_two, story_three]


    #will scrape images from the articles when done with project and more tools and libraries are available
    #https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f

    return render(request, 'MarvelComicsApp/MarvelComicsApp_news_comics.html', {'stories': stories})

def movie_news_view(request):
    page = requests.get('https://www.marvel.com/articles')
    soup = BeautifulSoup(page.content, 'html.parser')
    movie_news_section = soup.find_all(href=re.compile('.*\/articles\/movies.*'))
    # scrapping all comics news from the Marvel site. There are only three visible articles on the site at one time
    article_one = movie_news_section[1]
    article_two = movie_news_section[3]
    article_three = movie_news_section[5]
    # scrapping the text from the article summary and putting it into a dictionary

    story_one = {'summary': article_one.get_text(),
                 'link': article_one.get('href')
                 }
    story_two = {'summary': article_two.get_text(),
                 'link': article_two.get('href')
                 }
    story_three = {'summary': article_three.get_text(),
                   'link': article_three.get('href')
                   }
    stories = [story_one, story_two, story_three]

    # will scrape images from the articles when done with project and more tools and libraries are available
    # https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f

    return render(request, 'MarvelComicsApp/MarvelComicsApp_news_comics.html', {'stories': stories})

def tv_news_view(request):
    page = requests.get('https://www.marvel.com/articles')
    soup = BeautifulSoup(page.content, 'html.parser')
    tv_news_section = soup.find_all(href=re.compile('.*\/articles\/tv-shows.*'))
    # scrapping all comics news from the Marvel site. There are only three visible articles on the site at one time
    article_one = tv_news_section[1]
    article_two = tv_news_section[3]
    article_three = tv_news_section[5]
    # scrapping the text from the article summary and putting it into a dictionary

    story_one = {'summary': article_one.get_text(),
                 'link': article_one.get('href')
                 }
    story_two = {'summary': article_two.get_text(),
                 'link': article_two.get('href')
                 }
    story_three = {'summary': article_three.get_text(),
                   'link': article_three.get('href')
                   }
    stories = [story_one, story_two, story_three]

    # will scrape images from the articles when done with project and more tools and libraries are available
    # https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f

    return render(request, 'MarvelComicsApp/MarvelComicsApp_news_comics.html', {'stories': stories})

def game_news_view(request):
    page = requests.get('https://www.marvel.com/articles')
    soup = BeautifulSoup(page.content, 'html.parser')
    game_news_section = soup.find_all(href=re.compile('.*\/articles\/games.*'))
    # scrapping all comics news from the Marvel site. There are only three visible articles on the site at one time
    article_one = game_news_section[1]
    article_two = game_news_section[3]
    article_three = game_news_section[5]
    # scrapping the text from the article summary and putting it into a dictionary

    story_one = {'summary': article_one.get_text(),
                 'link': article_one.get('href')
                 }
    story_two = {'summary': article_two.get_text(),
                 'link': article_two.get('href')
                 }
    story_three = {'summary': article_three.get_text(),
                   'link': article_three.get('href')
                   }
    stories = [story_one, story_two, story_three]

    # will scrape images from the articles when done with project and more tools and libraries are available
    # https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f

    return render(request, 'MarvelComicsApp/MarvelComicsApp_news_comics.html', {'stories': stories})










