from django.urls import path


from . import views

urlpatterns = [
    path('', views.home, name='CodeBookApp_home'),
    path('CodeBookApp_author', views.add_author, name='CodeBookApp_author'),
    path('CodeBookApp_add', views.add_book, name='CodeBookApp_add'),
    path('CodeBookApp_books', views.code_books, name='CodeBookApp_books'),
    path('<int:pk>/book_detail/', views.book_detail, name='book_detail'),
    path('<int:pk>/book_edit/', views.book_edit, name='book_edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('confirm_delete/', views.confirmed, name='confirmed'),
]
