from django.urls import path
from . import views

urlpatterns = [
    path('concerts-home', views.home, name='concerts-home'),
    path('add', views.add_event, name="add_event"),
    path('see-database-items', views.display_items, name="see_database"),
    path('<int:pk>/details', views.details, name="concerts_events_details"),
    path('<int:pk>/edit_orchestra', views.edit_orchestra, name="edit_orchestra"),
    path('<int:pk>/edit_event', views.edit_event, name="edit_event"),
    path('<int:pk>/edit_piece', views.edit_piece, name="edit_piece"),
    path('<int:pk>/edit_conductor', views.edit_conductor, name="edit_conductor"),
    path('barbershop', views.barbershop_tags, name="barbershop")
]