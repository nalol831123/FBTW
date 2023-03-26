from django.shortcuts import render
from Player.models import Player
from Player.serializers import PlayerSerializer

from rest_framework import viewsets
# Create your views here.
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer