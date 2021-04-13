from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MyThai_home, name="MyThai_home"),
]