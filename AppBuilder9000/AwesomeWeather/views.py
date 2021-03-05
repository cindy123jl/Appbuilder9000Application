import requests
from django.shortcuts import render
from .models import City, Facts
from .forms import CityForm, FactForm

# Create your views here.
def about(request):
    if request.method == 'POST':
        form = FactForm(request.POST)
        form.save()

    form = FactForm()



    return render(request, 'AwesomeWeather/AwesomeWeather_about.html')



def home(request):



    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=84ed84d576a60dbcbf4149fa354c5cfe'

    if request.method == 'POST':  # only true if form is submitted
        form = CityForm(request.POST)  # add actual request data to form for processing
        form.save()  # will validate and save if validate

    form = CityForm()


    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }

        weather_data.append(city_weather)  # add the data for the current city into our list

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'AwesomeWeather/AwesomeWeather_home.html', context)  # returns the index.html template


