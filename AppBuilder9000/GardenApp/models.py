from django.db import models


zone_type = [('1a', '1a'), ('1b', '1b'), ('2a', '2a'), ('2b', '2b'), ('3a', '3a'), ('3b', '3b'), ('4a', '4a'),
('4b', '4b'),
]


class Planner(models.Model):
    zone = models.CharField(max_length=30)
    name = models.CharField(max_length=30, default='', blank=True, null=False)
    sowtime = models.CharField(max_length=10, default='', blank=True, null=False)

    class Meta:
        db_table = "planner"
