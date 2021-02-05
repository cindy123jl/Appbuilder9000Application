from django.db import models

# Create your models here.
class Review(models.Model):
    dated = models.DateField()
    business = models.ForeignKey('Venue', on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    review = models.TextField(max_length=255)
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    objects = models.Manager()

    def __str__(self):
        return self.title

VENUE_CHOICES = [
    ('Bar', 'Bar'),
    ('Dance Club', 'Dance Club'),
    ('Lounge', 'Lounge'),
]

#null makes sure form is filled out evertime
class Venue(models.Model):
    name = models.CharField(max_length=100, default='', null=False)
    street_address = models.CharField(max_length=150, null=False)
    zip = models.IntegerField()
    neighborhood = models.CharField(max_length=20, null=False)
    type = models.CharField(max_length=20, choices= VENUE_CHOICES, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.name
