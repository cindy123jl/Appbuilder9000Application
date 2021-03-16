from django.db import models


# A class for the accounts in our app
class AccountInfo(models.Model):

    username = models.CharField(max_length=100)

    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    account = models.Manager()

# A class for the budget used by the user
class BudgetInfo(models.Model):

    expenses = models.IntegerField()

    cost = models.FloatField()

    date_added = models.DateTimeField()

    user = models.ForeignKey(AccountInfo, on_delete=models.CASCADE)

    user_budget = models.IntegerField()

    budget = models.Manager()

