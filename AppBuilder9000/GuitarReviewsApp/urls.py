from django.urls import path
from . import views

urlspatterns = [
    path('', views.home, name='GuitarReviews_home.html'),
]