from django.db import models
# Creating my class model and adding my objects manager at the bottom
WILD_FARMED_CHOICES = (
    ('Wild', 'Wild'),
    ('Farmed', 'Farmed')
)


class Seafood(models.Model):
    name = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=100)
    harvested_during = models.DateField(blank=True)
    wild_caught = models.CharField(max_length=15, choices=WILD_FARMED_CHOICES)

    SeafoodIndex = models.Manager()

    def __str__(self):
        return self.name


