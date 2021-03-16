from django.urls import path
from . import views

urlpatterns = [
    path('gardenhome/', views.home, name='garden_home'),
    path('gardenplanner/', views.gardenplanner, name='gardenplanner'),
    path('contact/', views.contact, name='contact'),
]
