from django.db import models

TYPE_CHOICES = [
    ('City','City'),
    ('Country','Country'),
    ('State','State'),
]

Language_CHOICES = [
    ('English','English'),
    ('Spanish','Spanish'),
    ('French','French'),
    ('Russian','Russian'),
    ('Mandarin','Mandarin'),
    ('Korean','Korean'),
    ('German','German'),
    ('Italian','Italian'),
    ('Portuguese','Portuguese'),
]

class Destination(models.Model):
    name = models.CharField(max_length=60, default="",blank=True, null=False)
    description = models.TextField(max_length = 300, default="", null=False)
    language = models.CharField(max_length=60, choices=Language_CHOICES)
    type = models.CharField(max_length=60, choices=TYPE_CHOICES)


    objects = models.Manager()

    def __str__(self):
        return self.name