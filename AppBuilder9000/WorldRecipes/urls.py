from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='WR_home'),
    path('recipes', views.create_recipes, name='WR_create_recipes'),

]