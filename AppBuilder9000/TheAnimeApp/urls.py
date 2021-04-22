from django.urls import path
from . import views

urlpatterns = [
    path('', views.AnimeHome, name="AnimeHome"),
    path('AnimeBase/', views.AnimeBase, name="AnimeBase"),
    path('AnimeReviews/', views.AnimeReviews, name="AnimeReviews"),
    path('AnimeCreate/', views.AnimeCreate, name="AnimeCreate"),
]
