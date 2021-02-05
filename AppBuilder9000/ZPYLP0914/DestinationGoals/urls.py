from django.urls import path
from . import views

urlpatterns = [
    path('', views.DestinationGoals_home, name='DestinationGoals_home'),
    path('create_page', views.DestinationGoals_create, name='DestinationGoals_create'),
    path('Index', views.Destination_index, name='Destination_index'),
    path('<int:pk>/details/', views.DestinationGoals_details, name='DestinationGoals_details'),
    path('<int:pk>/edit/', views.DestinationGoals_edit, name='DestinationGoals_edit'),
    path('<int:pk>/delete/', views.DestinationGoals_delete, name='DestinationGoals_delete'),
    path('confirmDelete/', views.confirm_delete, name='DestinationGoals_confirmDelete'),

]