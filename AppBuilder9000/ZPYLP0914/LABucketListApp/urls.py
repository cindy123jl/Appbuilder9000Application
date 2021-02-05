from django.urls import path
from . import views

urlpatterns = [
    path('', views.bucketlist_home, name='BucketList_home'),
    path('Create', views.bucketlist_create, name='BucketList_create'),
    path('MasterList', views.bucketlist_index, name='BucketList_index'),
    path('<int:pk>/details/', views.bucketlist_details, name='BucketList_details'),
    path('<int:pk>/edit/', views.bucketlist_edit, name='BucketList_edit'),
    path('<int:pk>/delete/', views.bucketlist_delete, name='BucketList_delete'),

]
