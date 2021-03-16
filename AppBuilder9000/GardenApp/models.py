from django.db import models


zone_type = [('1a', '1a'), ('1b', '1b'), ('2a', '2a'), ('2b', '2b'), ('3a', '3a'), ('3b', '3b'), ('4a', '4a'),
('4b', '4b'),
]


class Planner(models.Model):
    zone = models.CharField(max_length=25)
    name = models.CharField(max_length=25, default='', blank=True, null=False)

    def __str__(self):
        return self.name
    objects = models.Manager()
