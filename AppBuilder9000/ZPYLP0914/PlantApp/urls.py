from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='PlantApp_home'),
    path('AddPlants', views.PlantApp_addPlant, name='PlantApp_AddPlants'),
    path('Plant Index', views.index, name='PlantApp_index'),
    path('Details/<int:pk>/', views.details, name='PlantApp_details'),
]

