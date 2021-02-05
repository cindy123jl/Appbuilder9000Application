from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='VegRestauranthome'), #url, method, page name
    path('create_order', views.createOrder, name='VegOrder'),
    path('data/', views.VR_index, name='VegData'),
    path('details/<int:order_id>', views.VR_details, name='VegDetails'),

]

