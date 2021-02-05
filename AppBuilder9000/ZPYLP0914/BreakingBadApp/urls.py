from django.urls import path
from . import views

urlpatterns = [
    path('', views.breakingbad_home, name='BreakingBadHome'),
    path('addepisode', views.breakingbad_addepisode, name='BreakingBadAddEpisode'),
    path('savedepisodes', views.breakingbad_savedepisodes, name='BreakingBadSavedEpisodes'),
    path('details-<int:pk>', views.breakingbad_details, name='BreakingBadDetails'),
    path('edit-<int:pk>', views.breakingbad_edit, name='BreakingBadEdit'),
    path('delete-<int:pk>', views.breakingbad_delete, name='BreakingBadDelete'),
]