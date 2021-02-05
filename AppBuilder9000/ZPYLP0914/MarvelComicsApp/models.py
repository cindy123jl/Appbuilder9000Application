from django.db import models

PREFERENCE = [
    ('Hero', 'Hero'),
    ('Villain', 'Villain'),
    ('Other', 'Other'),
]

TEAMS = [
    ('The Avengers', 'The Avengers'),
    ('The X-Men', 'The X-Men'),
    ('Inhumans', 'Inhumans'),
    ('Fantastic 4', 'Fantastic 4'),
    ('Guardians of the Galaxy', 'Guardians of the Galaxy'),
    ('Other', 'Other'),
]

class Character(models.Model):
    name = models.CharField(verbose_name='Character name', max_length=100, default="", blank=False, null=False)
    hero_name = models.CharField(verbose_name='Hero Name', max_length=50, blank=False, null=False)
    dob = models.DateField(verbose_name='Date of Birth', max_length=20)
    team = models.CharField(verbose_name='What super team are they affiliated with?', max_length=50, choices=TEAMS, default='')
    preference = models.CharField(verbose_name='Are they a hero or a villain?', max_length=10, choices=PREFERENCE, default='')
    powers = models.CharField(verbose_name='Powers', max_length=100, blank=False, null=False)
    bio = models.TextField(verbose_name='Biography', blank=False, null=False)

    object = models.Manager()

    def __str__(self):
        return self.name

class Favorite(models.Model):
    name = models.CharField(verbose_name='Character name', max_length=100, default="", blank=True, null=False)
    description = models.CharField(verbose_name='Description', max_length=500, default="", blank=True)
    path = models.CharField(verbose_name='Path', max_length=100)
    extension = models.CharField(verbose_name='Extension', max_length=50,
                                default='')
    api_id = models.CharField(verbose_name='ID', max_length=50,
                                      default='', blank=False)
    link = models.CharField(verbose_name='Link', max_length=150, default=True, blank=True)

    object = models.Manager()

    def __str__(self):
        return self.name




