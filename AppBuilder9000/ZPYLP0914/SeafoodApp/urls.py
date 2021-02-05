from django.urls import path
from . import views

urlpatterns = [
    path('', views.seafood_home, name='SeafoodAppHome'),
    path('seafoodlookup/', views.seafoodlookup, name='seafoodlookup'),
    path('seafoodadd/', views.seafoodadd, name='seafoodadd'),
    path('search/', views.seafoodsearch, name="SeafoodApp_search"),
    path('details/<int:pk>/', views.details, name="SeafoodApp_details"),
]

