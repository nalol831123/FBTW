from django.shortcuts import render
from GamerTeam.models import Gamer, Team
from GamerTeam.serializers import GamerSerializer, TeamSerializer

from rest_framework import viewsets
# Create your views here.
class GamerViewSet(viewsets.ModelViewSet):
    queryset = Gamer.objects.all()
    serializer_class = GamerSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
