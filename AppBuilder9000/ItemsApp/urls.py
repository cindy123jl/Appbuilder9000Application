from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="itemsApp_home"),
    path('new_item/', views.new_item, name="new_item"),
    path('view_items/', views.display_items, name="display_items"),
    path('details/', views.select_item, name="select_item"),
    path('details/<int:pk>/', views.item_details, name="item_details"),
]
