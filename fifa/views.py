from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from fifa.models import Player, Match, Team
from fifa.serializers import PlayerSerializer, MatchSerializer, TeamSerializer


def update_player():
	for i in range(11):
		dummy_player = Player(name='test1', ranking=1, age=22, jersey_number=10, position='Forward')
		dummy_player.save()


def update_teams():
	pass


def update_matches():
	pass


@csrf_exempt
def players_list(request):
	if request.method == 'GET':
		players = Player.objects.all()
		serializer = PlayerSerializer(players, many=True)
		return JsonResponse(serializer.data, safe=False)
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = PlayerSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def team_list(request):
	if request.method == 'GET':
		teams = Team.objects.all()
		serializer = TeamSerializer(teams, many=True)
		return JsonResponse(serializer.data, safe=False)
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = PlayerSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def matches_list(request):
	if request.method == 'GET':
		matches = Match.objects.all()
		serializer = MatchSerializer(matches, many=True)
		return JsonResponse(serializer.data, safe=False)
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = PlayerSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def player_detail(request, pk):
	try:
		player = Player.objects.get(pk=pk)
	except Player.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = PlayerSerializer(player)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = PlayerSerializer(player, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		player.delete()
		return HttpResponse(status=204)


@csrf_exempt
def team_detail(request, pk):
	try:
		team = Team.objects.get(pk=pk)
	except Team.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = TeamSerializer(team)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = TeamSerializer(team, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		team.delete()
		return HttpResponse(status=204)


@csrf_exempt
def match_detail(request, pk):
	try:
		match = Match.objects.get(pk=pk)
	except Player.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = MatchSerializer(match)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = MatchSerializer(match, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		match.delete()
		return HttpResponse(status=204)