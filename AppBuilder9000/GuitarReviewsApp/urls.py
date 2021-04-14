from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='GuitarReviews_home'),
    path('create', views.create, name='GuitarReviews_create')
]
