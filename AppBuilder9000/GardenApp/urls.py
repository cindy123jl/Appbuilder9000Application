from django.urls import path
from .import views


urlpatterns = [
    path('gardenhome/', views.home, name='gardenhome'),
    path('gardenplanner/', views.createplanner, name='gardenplanner'),
    path('gardentracker/', views.createtracker, name='gardentracker'),
    path('allvegetables/', views.allvegetables, name='allvegetables'),
    path('<int:pk>/gardendetails/', views.vegetabledetails, name='gardendetails'),
    path('<int:pk>/gardenedit/', views.vegetableedit, name='gardenedit'),
    path('<int:pk>/gardendelete/', views.vegetabledelete, name='gardendelete'),

]