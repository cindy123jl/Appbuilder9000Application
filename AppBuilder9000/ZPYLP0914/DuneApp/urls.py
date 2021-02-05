from django.urls import path
from . import views

urlpatterns = [
    path('', views.DuneApp_home, name='DuneApp_home'),
    path('DuneApp_createbook', views.DuneApp_createbook, name='DuneApp_createbook'),
    path('DuneAppBook_index', views.BookIndex, name='DuneAppBook_index'),
    path('<int:pk>/DuneApp_details', views.BookDetails, name='DuneApp_details'),
]