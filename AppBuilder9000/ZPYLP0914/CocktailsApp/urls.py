from django.urls import path
from . import views

urlpatterns = [
    path('', views.CocktailsApp_home, name='CocktailsApp_home'),
    path('Create', views.create, name='CocktailsApp_create'),
    path('Index', views.index, name='CocktailsApp_index'),
    path('Details/<int:pk>/', views.details, name='CocktailsApp_details'),
    path('Edit/<int:pk>/', views.edit, name='CocktailsApp_edit'),
    path('<int:pk>/delete/', views.delete, name='CocktailsApp_delete'),
    path('API', views.CocktailsApp_api, name='CocktailsApp_api'),




]