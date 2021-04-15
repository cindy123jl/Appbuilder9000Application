from django.db import models

# Create your models here.

class Stock(models.Model):
    name = models.CharField(max_length=5)
    market_cap = models.CharField(max_length=30)
    time_stamp = models.TimeField(max_length=40)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    Stock = models.Manager()



