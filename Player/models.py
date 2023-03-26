from django.db import models

# Create your models here.
class Player(models.Model):
    Player = models.CharField(max_length=20)
    Pts = models.FloatField()
    TwoP = models.FloatField()
    ThreeP = models.FloatField()
    REB = models.FloatField()
    AST = models.FloatField()
    STL = models.FloatField()
    BLK = models.FloatField()
    Fouls = models.FloatField()

    CreatedAt = models.DateTimeField(auto_now_add=True)