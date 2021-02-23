from django.urls import path
from . import views


urlpatterns = [
    path('', views.CampSite_home, name='CampSite_home'),
]
