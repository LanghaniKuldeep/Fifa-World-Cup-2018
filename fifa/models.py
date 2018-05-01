from django.db import models


class Player(models.Model):

	name = models.TextField()
	age = models.IntegerField()
	position = models.TextField()
	jersey_number = models.IntegerField()


class Team(models.Model):

	name = models.TextField()
	Players = models.ManyToManyField(Player)
	Manager = models.TextField
	group = models.TextField()
	ranking = models.IntegerField()


class Match(models.Model):

	home_team = Team()
	away_team = Team()
	datetime = models.DateTimeField()
	stadium = models.TextField()
	venue = models.TextField()

