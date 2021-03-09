from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('quantum_computer', views.quantumapp_home, name='quantumapp_home'),
]
