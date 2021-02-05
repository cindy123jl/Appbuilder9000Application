from django.db import models

# limit choices for spirit and flavor profile
SPIRIT_CHOICES = [
    ('vodka','vodka'),
    ('whiskey','whiskey'),
    ('tequila','tequila'),
    ('mezcal','mezcal'),
    ('gin','gin'),
    ('rum','rum'),
    ('other','other'),
]

FLAVOR_PROFILE_CHOICES = [
    ('sweet','sweet'),
    ('sour','sour'),
    ('spicy','spicy'),
    ('bitter','bitter'),
    ('boozy','boozy'),

]

RATING_CHOICES = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
]

# Define models

# model to create a cocktail
class Cocktail(models.Model):
    name = models.CharField(max_length=60, default="")
    spirit = models.CharField(max_length=60, choices=SPIRIT_CHOICES)
    ingredients = models.TextField(max_length=1000)
    flavor_profile = models.CharField(max_length=200, choices=FLAVOR_PROFILE_CHOICES)
    rating = models.IntegerField(choices=RATING_CHOICES)

    objects = models.Manager()

    def __str__(self):
        return self.name



# model to create a review for a cocktail
# class Review(models.Model):
#     name = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=60, default="")
#     review = models.TextField(max_length=1000)
#     rating = models.IntegerField(choices=RATING_CHOICES)
#
#
#     def __str__(self):
#         return self.first_name

