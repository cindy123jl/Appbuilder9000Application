from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views


urlpatterns = [
    # first argument goes in webaddress, last goes in django url reference
    path("hiking_home/", views.home, name="hiking_home"),

]
