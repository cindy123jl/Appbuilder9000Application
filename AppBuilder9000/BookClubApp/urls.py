from django.urls import path
from . import views

# create url paths
urlpatterns = [
    path('', views.home, name='home'),
    path('booklist/', views.booklist, name='bookList'),
    path('wishlist/', views.explore, name='explore'),
]