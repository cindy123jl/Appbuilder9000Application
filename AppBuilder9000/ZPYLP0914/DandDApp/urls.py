from django.urls import path
from . import views

urlpatterns = [
    path('', views.d_and_d_home, name='d_and_d_home'),
    path('add_character', views.add_character, name='add_character'),
    path('d_and_d_index', views.d_and_d_index, name='d_and_d_index'),
    path('<int:pk>/d_and_d_details', views.d_and_d_details, name='d_and_d_details'),
    path('<int:pk>/d_and_d_edit', views.d_and_d_edit, name='d_and_d_edit'),
    path('<int:pk>/d_and_d_delete', views.d_and_d_delete, name='d_and_d_delete'),
    path('d_and_d_article', views.d_and_d_article, name='d_and_d_article'),


]
