from django.db import models

# Create your models here.

# Limit the choices for growth type

GROWTH_CHOICES = (
    ('Trailing/Vining', 'Trailing/Vining'),
    ('Tree', 'Tree'),
    ('Shrub', 'Shrub'),
    ('Succulent', 'Succulent'),
    ('Fern', 'Fern'),
)

# limit the choices for light needs

LIGHT_CHOICES = (
    ('Direct Light', 'Direct Light'),
    ('Bright Indirect Light', 'Bright Indirect Light'),
    ('Indirect Light', 'Indirect Light'),
)


# define model

class Indoor_Plant(models.Model):
    plant_name = models.CharField(max_length=50)
    plant_growth = models.CharField(max_length=25, choices=GROWTH_CHOICES)
    plant_light = models.CharField(max_length=30, choices=LIGHT_CHOICES)
    plant_description = models.TextField(max_length=300)

    objects = models.Manager()

    def __str__(self):
        return self.plant_name
