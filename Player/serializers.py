from rest_framework import serializers
from Player.models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        # fields = '__all__'
        fields = ('Player', 'Pts', 'TwoP', 'ThreeP', 'REB', 'AST', 'STL', 'BLK', 'Fouls')
