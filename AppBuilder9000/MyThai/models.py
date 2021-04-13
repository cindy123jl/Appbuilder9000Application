from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Restaurant(models.Model):
    name = models.CharField(max_length=40, default='')
    phone = models.CharField(max_length=12, default='(000)000-0000')
    address = models.CharField(max_length=95, default='')
    city = models.CharField(max_length=15, default='Portland')
    rating = models.IntegerField(
        default='',
        validators=[MaxValueValidator(10), MinValueValidator(0)]  # Check to make sure rating in range.
    )

    object = models.Manager()

    def __str__(self):
        return self.name
