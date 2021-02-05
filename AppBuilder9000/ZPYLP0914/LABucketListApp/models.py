from django.db import models

# limit choices for type and price
TYPE_CHOICES = [
    ('Site', 'Site'),
    ('Activity', 'Activity'),
    ('Food', 'Food'),
    ('Museum', 'Museum'),
]

PRICE_CHOICES = [
    ('Free', 'Free'),
    ('Under $25', 'Under $25'),
    ('$25 to $50', '$25 to $50'),
    ('$50 to $100', '$50 to $100'),
    ('$100+', '$100+'),
]

# model to create a new destination
class Destination(models.Model):
    name = models.CharField(max_length=200, default="", blank=False)
    type = models.CharField(max_length=60, choices=TYPE_CHOICES)
    description = models.TextField(max_length=300, default="")
    location = models.CharField(max_length=200)
    price = models.CharField(max_length=60, choices=PRICE_CHOICES)

    objects = models.Manager()

    def __str__(self):
        return self.name

