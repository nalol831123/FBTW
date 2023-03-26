from rest_framework import serializers
from create_league.models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        # fields = '__all__'
        fields = ('GroupName', 'League', 'Ceo', 'DraftTime', 'DraftMode', 'GameMode', 'SeasonEnd')
