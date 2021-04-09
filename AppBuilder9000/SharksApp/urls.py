from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('SharksApp_home', views.SharksApp_home, name="SharksApp_home"),
    path('SharksApp_newitem/', views.Create_Shark, name="SharksApp_newitem"),
]
