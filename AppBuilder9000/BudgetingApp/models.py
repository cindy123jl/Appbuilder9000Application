from django.db import models


# A class for the accounts in our app
class AccountInfo(models.Model):

    username = models.CharField(max_length=100)

    password = models.CharField(max_length=100)

    user_budget = models.IntegerField()

    def __str__(self):
        return self.username

    account = models.Manager()

# A class for the budget used by the user


class BudgetInfo(models.Model):

    expense_name = models.CharField(max_length=30, default='Expense Name')

    cost = models.FloatField()

    date_added = models.DateTimeField()

    username = models.CharField(max_length=20, default='Your Name!')

    def __str__(self):
        return self.expense_name

    objects = models.Manager()

