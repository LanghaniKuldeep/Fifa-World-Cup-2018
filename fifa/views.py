import urllib2
from collections import OrderedDict
from datetime import datetime, timedelta

from bs4 import BeautifulSoup
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

HDR = {
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	'Accept-Encoding': 'none',
	'Accept-Language': 'en-US,en;q=0.8',
	'Connection': 'keep-alive'}


@csrf_exempt
def get_fixtures(request):
	matches = 'http://www.fifa.com/worldcup/matches/'
	req = urllib2.Request(matches, headers=HDR)
	page = urllib2.urlopen(req)
	matches_content = page.read()
	matches_page = BeautifulSoup(matches_content)
	group_stages, knockouts_stages = matches_page.find_all('div', class_='fi-matchlist')
	group_stages = group_stages.find_all('div', class_='fi-mu-list')
	knockouts_stages = knockouts_stages.find_all('div', class_='fi-mu-list')
	match_fixtures = OrderedDict()
	group_match_fixtures = OrderedDict()
	knock_match_fixtures = OrderedDict()

	for match_day in group_stages:
		date_match = match_day.find('span', class_='fi-mu-list__head__date').text
		date_match = get_clean_text(get_clean_text(date_match).split('day')[1])
		matches = match_day.find_all('a', class_='fi-mu__link')
		match_per_day = []
		for match in matches:
			match_data = OrderedDict()
			time = match.find('div', class_='fi-mu__info__datetime').attrs['data-utcdate']
			time = (datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.000Z") + timedelta(hours=12)).isoformat()
			match_data['link'] = match.attrs['href']
			match_data['datetime'] = time
			match_data['group'] = match.find('div', class_='fi__info__group').text
			match_data['home_team'] = match.find_all('span', class_='fi-t__nText')[0].text
			match_data['away_team'] = match.find_all('span', class_='fi-t__nText')[1].text
			home_flag, away_flag = match.find_all('img', class_='fi-flag--4')
			match_data['home_flag'] = home_flag.attrs['src']
			match_data['away_flag'] = away_flag.attrs['src']
			match_data['stadium'] = match.find('div', class_='fi__info__stadium').text
			match_data['venue'] = match.find('div', class_='fi__info__venue').text
			match_per_day.append(match_data)
		group_match_fixtures[date_match] = match_per_day

	for match_day in knockouts_stages:
		date_match = match_day.find('span', class_='fi-mu-list__head__date').text
		date_match = get_clean_text(date_match)
		matches = match_day.find_all('div', class_='fi-mu fixture')
		match_per_day = []
		for match in matches:
			match_data = OrderedDict()
			time = match.find('div', class_='fi-mu__info__datetime').attrs['data-utcdate']
			time = (datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.000Z") + timedelta(hours=12)).isoformat()
			match_data['datetime'] = time
			match_data['home_team'] = match.find_all('span', class_='fi-t__nText')[0].text
			match_data['away_team'] = match.find_all('span', class_='fi-t__nText')[1].text
			home_flag, away_flag = match.find_all('img', class_='fi-flag--4')
			match_data['home_flag'] = home_flag.attrs['src']
			match_data['away_flag'] = away_flag.attrs['src']
			match_data['stadium'] = match.find('div', class_='fi__info__stadium').text
			match_data['venue'] = match.find('div', class_='fi__info__venue').text
			match_per_day.append(match_data)
		knock_match_fixtures[date_match] = match_per_day

	match_fixtures['group_stages'] = group_match_fixtures
	match_fixtures['knockout_stages'] = knock_match_fixtures
	data = {'Author': "Kuldeep Kumar", 'data': match_fixtures}
	return JsonResponse(data)


@csrf_exempt
def get_group_standings(request):
	group_standing = 'http://www.fifa.com/worldcup/groups/'
	req = urllib2.Request(group_standing, headers=HDR)
	page = urllib2.urlopen(req)
	groups_standing_content = page.read()
	groups_standing_content = BeautifulSoup(groups_standing_content)
	groups = groups_standing_content.find_all('table', class_='fi-table fi-standings')
	groups_table = []
	for group_cat in groups:
		group_stats = OrderedDict()
		group_stats['title'] = group_cat.find('p', class_="fi-table__caption__title").text
		teams = group_cat.tbody.findAll('tr')
		for i in range(0, 4):
			name = teams[i].find('span', class_='fi-t__nText').text
			group_stats[name] = OrderedDict()
			group_stats[name]['display_name'] = name
			group_stats[name]['flag'] = teams[i].find('img', class_='fi-flag--4').attrs['src']
			group_stats[name]['matches_played'] = teams[i].find('td', class_='fi-table__matchplayed').find('span').text
			group_stats[name]['matches_win'] = teams[i].find('td', class_='fi-table__win').find('span').text
			group_stats[name]['matches_draw'] = teams[i].find('td', class_='fi-table__draw').find('span').text
			group_stats[name]['matches_lost'] = teams[i].find('td', class_='fi-table__lost').find('span').text
			group_stats[name]['goal_for'] = teams[i].find('td', class_='fi-table__goalfor').find('span').text
			group_stats[name]['goal_against'] = teams[i].find('td', class_='fi-table__goalagainst').find('span').text
			group_stats[name]['goal_difference'] = teams[i].find('td', class_='fi-table__diffgoal').find('span').text
			group_stats[name]['points'] = teams[i].find('td', class_='fi-table__pts').find('span').text
		groups_table.append(group_stats)
	data = {'Author': "Kuldeep Kumar", 'data': groups_table}
	return JsonResponse(data)


@csrf_exempt
def get_news(request):
	news_posts = []
	for i in range(1,3):
		news_url = 'https://www.fifa.com/worldcup/news/page/'+str(i)
		req = urllib2.Request(news_url, headers=HDR)
		page = urllib2.urlopen(req)
		page_content = page.read()
		page_content = BeautifulSoup(page_content)
		news_divs = page_content.find_all('div', class_='col-xs-12 col-sm-4 col-md-3 col-flex')
		for news_item in news_divs:
			news = {}
			news['image_link'] = news_item.find('img')['data-src']
			news['news_link'] = news_item.find('a', class_='fi-o-media-object__link')['href']
			news['news_title'] = news_item.find('h3', class_='d3-o-media-object__title fi-o-media-object__title').text
			news['date'] = news_item.find('p', class_='d3-o-media-object__date fi-o-media-object__date').text
			news_posts.append(news)
	data = {'Author': "Kuldeep Kumar", 'data': news_posts}
	return JsonResponse(data)


@csrf_exempt
def get_live_score(request, match_id):

	url = 'http://www.fifa.com/worldcup/matches/match/' + str(match_id)
	req = urllib2.Request(url, headers=HDR)
	page = urllib2.urlopen(req)
	page_content = page.read()
	match_update = {}
	page_content = BeautifulSoup(page_content)
	update = page_content.find('div', class_='fi-mu__m')
	statuses = update.find('div', class_='fi-s__status').findAll('span', class_='period')
	for status in statuses:
		if 'hidden' not in status.attrs['class']:
			match_update['status'] = get_clean_text(status.text)
	if not match_update.get('status'):
		match_update['status'] = get_clean_text(update.find('span', class_='period minute hidden').text)
	match_update['score'] = get_clean_text(update.find('span', class_='fi-s__scoreText').text)
	home_goals = page_content.find('div', class_='fi-mh__scorers__home').findAll('li', class_='fi-mh__scorer')
	away_goals = page_content.find('div', class_='fi-mh__scorers__away').findAll('li', class_='fi-mh__scorer')

	match_update['home_scoreres'] = get_goal_scorer(home_goals)
	match_update['away_scoreres'] = get_goal_scorer(away_goals)

	data = {'Author': "Kuldeep Kumar", 'data': match_update}
	return JsonResponse(data)


def get_goal_scorer(goals):
	players = []
	for goal_socerer in goals:
		player = {}
		player['title'] = get_clean_text(goal_socerer.find('span', class_='fi-p__nShorter ').text)
		player['minute'] = get_clean_text(goal_socerer.find('span', class_='fi-mh__scorer__minute').text)
		players.append(player)
	return players


def get_clean_text(text):
	return text.replace('\r','').replace(' ','').replace('\n','')
