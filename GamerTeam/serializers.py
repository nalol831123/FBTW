from rest_framework import serializers
from GamerTeam.models import Gamer, Team


class GamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamer
        # fields = '__all__'
        fields = ('GroupName', 'Ceo', 'Gamer', 'Score')

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        # fields = '__all__'
        fields = ('GroupName', 'Gamer', 'Player', 'Status')
