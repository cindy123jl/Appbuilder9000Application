from django.urls import path
from . import views

urlpatterns = [
    path('', views.nightlife_home, name='SeattleNightLife_home'),
    path('create/', views.nightlife_create, name='SeattleNightLife_create'),
    path('index/', views.nightlife_index, name='SeattleNightLife_index'),
    path('<int:pk>/details/', views.nightlife_details, name='SeattleNightLife_details'),
    path('<int:pk>/edit/', views.nightlife_edit, name='SeattleNightLife_edit'),
    path('<int:pk>/delete/', views.nightlife_delete, name='SeattleNightLife_delete'),
    path('confirmDelete/', views.confirm_delete, name='SeattleNightLife_confirmDelete'),
    ]