from rest_framework import serializers

from fifa.models import Player, Team, Match


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
