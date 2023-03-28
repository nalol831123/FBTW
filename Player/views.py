from django.shortcuts import render
from Player.models import Player
from Player.serializers import PlayerSerializer

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

# get player data
class Crawler(APIView):
    def get(self, request):
        try:
            print('----------------start Crawling---------------', flush=True)
            return Response(status=200)
        except Exception as err:
            return Response(str(err), status=400)

            