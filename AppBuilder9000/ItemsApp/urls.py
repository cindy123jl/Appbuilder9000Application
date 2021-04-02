from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="itemsApp_home"),
    path('new_item/', views.new_item, name="new_item"),
    path('create_item/', views.createItem, name="create_item"),
    path('view_items/', views.viewItem, name="view_items"),
    path('<int:pk>/details/', views.details, name="details"),
]
