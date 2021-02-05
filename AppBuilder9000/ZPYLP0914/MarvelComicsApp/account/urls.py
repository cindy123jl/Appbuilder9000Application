from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.registration_view, name='MarvelComicsAppRegister'),
    path('logout/', views.logout_view, name='MarvelComicsAppLogout'),
    path('login/', views.login_view, name='MarvelComicsAppLogin')
]