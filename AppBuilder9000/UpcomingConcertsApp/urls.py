from django.urls import path
from . import views

urlpatterns = [
    path('concerts-home', views.home, name='concerts-home'),
    path('add', views.add_event, name="add_event"),
    path('see-database-items', views.display_items, name="see_database"),
]