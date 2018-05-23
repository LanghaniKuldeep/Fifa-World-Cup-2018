from django.conf.urls import url
from fifa import views


urlpatterns = [
	url(r'^grouptable$', views.get_group_standings),
	url(r'^fixtures$', views.get_fixtures),
]