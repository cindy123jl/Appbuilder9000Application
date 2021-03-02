from django.db import models
import datetime

# Create your models here.

class quantuminfo(models.Model):
    quantum_computers = models.CharField(max_length=200)
    quantumtheorie = models.CharField(max_length=200)
    superposition = models.CharField(max_length=200)


