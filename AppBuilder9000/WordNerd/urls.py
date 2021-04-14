from django.urls import path
from .import views

urlpatterns = [
    path('', views.WordNerd_home, name='WordNerd_home'),
    path('WordNerd_createword/', views.WordNerd_createword, name='WordNerd_createword'),
    path('WordNerd_viewdata/', views.WordNerd_viewdata, name='WordNerd_viewdata')
]
