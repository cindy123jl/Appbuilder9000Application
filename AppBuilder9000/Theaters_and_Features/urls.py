from django.urls import path
from . import views

urlpatterns = [
    path('', views.Theater_home, name='Theater_home'),
]

