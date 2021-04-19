from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='StockApp_home'),
    path('StockApp_base/', views.base, name='StockApp_base'),
    path('StockApp_newstock/', views.new, name='StockApp_newstock'),
]
