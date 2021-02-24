from django.db import models

STATE_CHOICES = [
    ('CA', 'California'),
    ('OR', 'Oregon'),
    ('WA', 'Washington'),
]

TYPE_CHOICES = [
    ('Dispersed', 'Dispersed'),
    ('Developed', 'Developed'),
]

ACCESS_CHOICES = [
    ('Drive-up', 'Drive-up'),
    ('Hike-in', 'Hike-in'),
]

RATING_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
]


class Campsite(models.Model):

    name = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    type = models.CharField(max_length=9, choices=TYPE_CHOICES)
    access = models.CharField(max_length=8, choices=ACCESS_CHOICES)
    description = models.CharField(max_length=500)
    fee = models.DecimalField(max_digits=5, decimal_places=2)
    directions = models.CharField(max_length=500, null=True, blank=True)

    Campsites = models.Manager()

    def __str__(self):
        return self.name + "," + self.state


class MySite(models.Model):
    name = models.ForeignKey(Campsite, on_delete=models.CASCADE)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    type = models.CharField(max_length=9, choices=TYPE_CHOICES)
    access = models.CharField(max_length=8, choices=ACCESS_CHOICES)
    rating = models.IntegerField(max_length=2, choices=RATING_CHOICES)
    notes = models.CharField(max_length=250, null=True, blank=True)

    MySites = models.Manager()

    def __str__(self):
        return self.name
