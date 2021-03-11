from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='BudgetingApp_home'),
]