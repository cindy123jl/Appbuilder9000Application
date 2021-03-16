from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='gardenhome'),
    path('gardenplanner/', views.gardenplanner, name='gardenplanner'),
    path('contact/', views.contact, name='contact'),
]
