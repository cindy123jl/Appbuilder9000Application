from django.urls import path
from . import views

urlpatterns = [
    path('garden_home', views.home, name='garden_home'),
]
