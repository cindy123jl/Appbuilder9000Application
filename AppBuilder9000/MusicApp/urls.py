from django.urls import path
from . import views


urlpatterns = [
    path('', views.MusicApp_home, name='MusicApp_home'),
]
