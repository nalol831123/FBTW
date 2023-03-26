from django.db import models

# Create your models here.
class Gamer(models.Model):
    GroupName = models.CharField(max_length=20)
    Ceo = models.CharField(max_length=20)
    Gamer = models.CharField(max_length=20)
    Score = models.IntegerField()

    CreatedAt = models.DateTimeField(auto_now_add=True)

class Team(models.Model):
    GroupName = models.CharField(max_length=20)
    Gamer = models.CharField(max_length=20)
    Player = models.CharField(max_length=20)
    Status = models.CharField(max_length=20)

    CreatedAt = models.DateTimeField(auto_now_add=True)