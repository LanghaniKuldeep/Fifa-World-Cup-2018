from django.conf.urls import url
from fifa import views


urlpatterns = [
	url(r'$', views.players_list),
	url(r'^update_players$', views.update_player),
	url(r'^update_teams$', views.update_teams),
	url(r'^update_matches$', views.update_matches),
	url(r'^players/$', views.players_list),
	url(r'^players/(?P<pk>[0-9]+)/$', views.player_detail),
	url(r'^teams/$', views.team_list),
	url(r'^teams/(?P<pk>[0-9]+)/$', views.team_detail),
	url(r'^matches/$', views.matches_list),
	url(r'^matches/(?P<pk>[0-9]+)/$', views.match_detail),
]