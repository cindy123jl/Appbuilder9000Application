from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='AstronomyApp'),
    path('AddPlanet', views.manage_planets, name='add_planet'),
    path('index', views.planet_index, name='planet_index'),
    path('details/<int:pk>/', views.details, name='details'),
]
