from django.urls import path
from .import views


urlpatterns = [
    path('home.html', views.home, name='BudgetingApp_home'),
    path('login.html', views.login, name='BudgetingApp_login'),
    path('budget.html', views.create_budget, name='BudgetingApp_budget'),
    path('account.html', views.account, name='BudgetingApp_account'),

]