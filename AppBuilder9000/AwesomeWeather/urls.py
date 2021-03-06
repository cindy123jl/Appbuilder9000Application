from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='weather_home'),
    path('about/', views.about, name='about'),
    path('delete/<city_name>/', views.delete_city, name='delete_city'),
    path('post/new/', views.about, name='post_new'),
]