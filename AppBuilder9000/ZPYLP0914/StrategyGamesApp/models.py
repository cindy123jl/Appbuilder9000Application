from django.db import models

# Create your models here.
class StrategyGame(models.Model):
    Title = models.CharField(max_length=100)
    Theme = models.CharField(max_length=100)
    Date_Released = models.DateField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return self.Title