from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views


urlpatterns = [
    path("Hiking_home/", views.home, name="Hiking_home"),
]
