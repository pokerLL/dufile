from audioop import add
from django.db import models

# Create your models here.

class myFile(models.Model):
    name = models.CharField()
    address  = models.FileField()