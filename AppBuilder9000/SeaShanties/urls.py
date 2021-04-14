from django.urls import path
from .import views


urlpatterns = [
    path('', views.shantieshome, name='shanties_home'),
]
