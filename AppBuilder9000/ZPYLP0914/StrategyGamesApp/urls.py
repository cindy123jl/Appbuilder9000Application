from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='StrategyGamesHome'),
    path('create-strategygame', views.game_create, name='add game'),
    path('Display_Data', views.Display_Games, name='Display_Data'),
    path('Details/<int:pk>', views.details, name='DetailedGames'),
    ]