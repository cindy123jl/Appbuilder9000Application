from django.urls import path

from . import views

urlpatterns = [
    path('', views.coffee_home, name="coffee_home")
]
