from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='MarvelComicsAppHome'),
    path('create-character/', views.character_create_view, name='MarvelComicsAppCreateCharacter'),
    path('character-index/', views.character_index_view, name='MarvelComicsAppCharacterIndex'),
    path('character-details/<int:pk>/', views.character_detail_view, name="MarvelComicsAppCharacterDetail"),
    path('edit-character/<int:pk>/', views.character_edit_view, name='MarvelComicsAppEditCharacter'),
    path('delete-character/<int:pk>/', views.character_delete_view, name='MarvelComicsAppDeleteCharacter'),
    path('search/', views.search_view, name='MarvelComicsAppSearch'),
    path('results/<str:data>/', views.results_view, name='MarvelComicsAppResults'),
    path('random/', views.random_view, name='MarvelComicsAppRandom'),
    path('comic-news/', views.comic_news_view, name='MarvelComicsAppComicNews'),
    path('movie-news/', views.movie_news_view, name='MarvelComicsAppMovieNews'),
    path('tv-news/', views.tv_news_view, name='MarvelComicsAppTVNews'),
    path('game-news/', views.game_news_view, name='MarvelComicsAppGameNews'),
]
