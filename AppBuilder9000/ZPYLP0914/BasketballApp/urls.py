from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='BasketballApp_home'),
    path('add_player', views.add_player, name='add_player'),
    path('BasketballApp_index', views.index, name='BasketballApp_index'),
    path('<int:pk>/BasketballApp_details', views.BasketballApp_details, name='BasketballApp_details'),
]