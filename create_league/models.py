from django.db import models

# Create your models here.
class Group(models.Model):
    GroupName = models.CharField(max_length=20)
    League = models.CharField(max_length=20)
    Ceo = models.CharField(max_length=20)
    DraftTime = models.DateTimeField()
    DraftMode = models.CharField(max_length=20)
    GameMode = models.CharField(max_length=20)
    SeasonEnd = models.DateTimeField()

    CreatedAt = models.DateTimeField(auto_now_add=True)