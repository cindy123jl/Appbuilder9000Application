from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MyThai_home, name="MyThai_home"),
    path('add/', views.new_restaurant, name="MyThai_add"),
]