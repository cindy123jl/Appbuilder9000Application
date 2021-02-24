from . import views

urlpatterns = [
    path('', views.home, name="coffeeshop_home")
]
