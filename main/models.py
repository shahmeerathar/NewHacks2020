from django.db import models


# Create your models here.
class User(models.Model):
    '''Creates a table with username, room, and score'''
    username = models.CharField(max_length=50)
    room = models.CharField(max_length=50)
    score = models.DecimalField(default=0.0, decimal_places=3, max_digits=100)
