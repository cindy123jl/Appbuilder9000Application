from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='CryptoApp_home'),
    path('create/', views.add_currency, name='CryptoApp_AddCurrency'),
    path('update/', views.add_status, name='CryptoApp_AddStatus'),
    path('display/', views.display, name='CryptoApp_display')
]
