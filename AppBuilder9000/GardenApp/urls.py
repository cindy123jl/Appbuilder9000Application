from django.urls import path
from .import views


urlpatterns = [
    path('gardenhome/', views.home, name='garden_home'),
    path('gardenplanner/', views.createplanner, name='gardenplanner'),
    path('gardentracker/', views.createevalform, name='gardentracker'),
    path('gardencare/', views.get_gardenplanner, name='gardencare'),
    path('gardensearch/', views.SearchView.as_view(), name='search'),
    path('<int:pk>/gardendetails/', views.vegetable_details, name='gardendetails')
]