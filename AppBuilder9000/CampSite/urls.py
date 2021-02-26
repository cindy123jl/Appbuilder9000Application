from django.urls import path
from . import views


urlpatterns = [
    path('', views.campsite_home, name='CampSite_home'),
    path('add_campsite/', views.add_campsite, name='add_campsite'),
    path('browse_campsites/', views.browse, name='browse')
]
