from django.db import models

# Create your models here.

DIFFICULTY_CHOICES = {
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
}
STATE_CHOICES = {
    ('Washington', 'WA'),
    ('Missouri', 'MO'),
    ('Michigan', 'MI'),
    ('California', 'CA'),
    ('New York', 'NY'),
    ('Pennsylvania', 'PA'),
}


# making blueprint of a type called Trails
class Trails(models.Model):
    name = models.CharField(max_length=60)
    state = models.CharField(max_length=10, choices=STATE_CHOICES)
    miles = models.DecimalField(default=0.0, max_digits=3, decimal_places = 2)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    camping = models.BooleanField()

    objects = models.Manager()
    def __str__(self):
        return self.name