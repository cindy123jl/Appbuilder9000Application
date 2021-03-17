from django.urls import path
from .import views

urlpatterns = [
    path('gardenhome/', views.home, name='garden_home'),
    path('gardencare/', views.care, name='gardencare'),
    path('gardenplanner/', views.createplanner, name='gardenplanner'),
    path('gardentracker/', views.createevalform, name='gardentracker'),
]
