from django.shortcuts import render
from create_league.models import Group
from create_league.serializers import GroupSerializer

from rest_framework import viewsets
# Create your views here.
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer