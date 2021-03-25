from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='CryptoApp_home'),
    path('create/', views.add_currency, name='CryptoApp_AddCurrency')
]
