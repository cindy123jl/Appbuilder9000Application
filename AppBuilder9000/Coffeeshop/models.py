from django.db import models

Drink_Type = {
    ('hot drinks', 'hot drinks'),
    ('cold drinks', 'cold drinks'),
    ('breakfast', 'breakfast'),
    ('extras', 'extras'),

}


class Drinks(models.Model):
    type = models.CharField(max_length=60, choices=Drink_Type),
    name = models.CharField(max_length = 60,default="",blank=True, null=False),
    description = models.TextField(max_length=300, default= "",blank=True),
    price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2),
    image = models.CharField(max_length=255, default='', blank=True)

    objects= models.Manager()

    def __str__(self):
        return self.name
