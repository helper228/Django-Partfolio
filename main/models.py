from django.db import models

# Create your models here.

class Massege(models.Model):
    Name = models.CharField(max_length=70)
    gmail = models.CharField(max_length=70)
    massege = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)

