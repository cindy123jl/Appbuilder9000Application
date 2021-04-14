from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MyThai_home, name="MyThai_home"),
    path('add_restaurant/', views.new_restaurant, name="MyThai_add_restaurant"),
    path('add_dish/', views.new_dish, name="MyThai_add_dish"),
]