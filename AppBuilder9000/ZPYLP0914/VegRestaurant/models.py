from django.db import models

# Create your models here.
DISH_CHOICES = [
    ('RastaPasta', 'RastaPasta'),
    ('CornSoup', 'CornSoup'),
    ('TaiNuggets', 'TaiNuggets'),
    ('SpicyTofuTacos', 'SpicyTofuTacos'),
]


class Order(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=50)
    phone_number=models.CharField(max_length=10, default="", blank=True, null=False)
    dish_name = models.CharField(max_length=20, choices=DISH_CHOICES)

    objects = models.Manager()

    def __str__(self):
        return self.dish_name

