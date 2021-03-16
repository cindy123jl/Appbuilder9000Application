from django.db import models


zone_type = [('1a', '1a'), ('1b', '1b'), ('2a', '2a'), ('2b', '2b'), ('3a', '3a'), ('3b', '3b'), ('4a', '4a'),
('4b', '4b'),('5a', '5a'),('5b', '5b'),('6a', '6a'),('6b', '6b'),('7a', '7a'),('7b', '7b'), ('8a', '8b'),
('9a', '9b'), ('9a', '9b'), ('10a', '10a'), ('10b', '10b'), ('11a', '11a'), ('11b', '11b'),
('12a', '12a'),('12b', '12b'), ('13a', '13a'), ('13b', '13b'),
]


class Planner(models.Model):
    zone = models.CharField(max_length=30)
    name = models.CharField(max_length=30, default='', blank=True, null=False)
    sowtime = models.CharField(max_length=10, default='', blank=True, null=False)

    class Meta:
        db_table = "planner"
