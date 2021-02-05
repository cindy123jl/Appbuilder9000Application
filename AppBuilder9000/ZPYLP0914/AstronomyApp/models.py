from django.db import models

# Create your models here.
from django.db import models



ATMOSPHERE_CHOICES = [
    ('Hydrogen', 'Hydrogen'),
    ('Sulfuric Acid', 'Sulfuric Acid'),
    ('Oxygen/Nitrogen', 'Oxygen/Nitrogen'),
    ('Carbon dioxide', 'Carbon dioxide'),
    ('Methane/Ammonia', 'Methane/Ammonia'),
    ('None', 'None'),
    ('Unknown', 'Unknown'),
]


class Planet(models.Model):
    name = models.CharField(verbose_name="Planet name", max_length=50)
    gravity = models.DecimalField(max_digits=3, decimal_places=1)
    temperature = models.CharField(max_length=15)
    atmosphere = models.CharField(max_length=50, choices=ATMOSPHERE_CHOICES)
    water = models.BooleanField(default=False)
    magnetic_field = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Star(models.Model):
    name = models.CharField(max_length=40)
    planets = models.ManyToManyField(Planet)


class Galaxy(models.Model):
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=40)
    distance = models.CharField(max_length=40)
    stars = models.ManyToManyField(Star)



