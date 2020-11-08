from django.db import models

# Create your models here.
class Leaderboard (models.Model):
    '''Creates a table with username, room, and score'''
    username = models.CharField(max_length=50)
    room = models.CharField(max_length=50)
    score = models.IntegerField()
