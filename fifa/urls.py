from django.conf.urls import url
from fifa import views


urlpatterns = [
	url(r'^grouptable$', views.get_group_standings),
	url(r'^fixtures$', views.get_fixtures),
	url(r'^news$', views.get_news),
	url(r'^live/worldcup/matches/match/(?P<match_id>\d+)/$', views.get_live_score)
]