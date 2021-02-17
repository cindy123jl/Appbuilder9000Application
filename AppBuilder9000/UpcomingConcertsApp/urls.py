from django.urls import path
from . import views

urlpatterns = [
    path('concerts-home', views.home, name='concerts-home'),
]