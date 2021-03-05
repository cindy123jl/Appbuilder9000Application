from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=25)


    def __str__(self):
        return self.name

    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'cities'

class Facts(models.Model):
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    date = models.CharField(max_length=50)
    event = models.CharField(max_length=200)





    fact = models.Manager()







