from django.db import models

Postition_Choice = [
    ('Point Guard', 'Point Guard'),
    ('Shooting Guard', 'Shooting Guard'),
    ('Small Forward', 'Small Forward'),
    ('Power Forward', 'Power Forward'),
    ('Center', 'Center'),
]

#null makes sure form is filled out evertime
class CreatePlayer(models.Model):
    name = models.CharField(max_length=50, default='', null=False)
    age = models.IntegerField(null=False)
    position = models.CharField(max_length=50, choices=Postition_Choice, null=False)
    weight = models.IntegerField(null=False)
    years_pro = models.IntegerField(null=False)

    object = models.Manager()

    def __str__(self):
        return self.name