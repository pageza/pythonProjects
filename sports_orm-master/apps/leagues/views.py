from django.shortcuts import render, redirect
from .models import League, Team, Player
import re
from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}
	# 1. baseball leagues
	# context = {
	# 	'leagues': League.objects.filter(sport='Baseball')
	# }
	# 2. Womens leagues
	# context = {
	# 	'leagues': League.objects.filter(name__regex=r'^.*Womens.*$')
	# }
	# 3. any type of hockey league
	# context = {
	# 	'leagues': League.objects.filter(name__regex=r'^.*Hockey.*$')
	# }
	# 4.league with sport OTHER than Football
	# context = {
	# 	'leagues': League.objects.exclude(sport='Football')
	# }
	# 5. all leagues that call themselves "conferences"
	# context = {
	# 	'leagues': League.objects.filter(name__regex=r'^.+Conference.+$')
	# }
	# 6. ...all leagues in the Atlantic region
	# context = {
	# 	'leagues': League.objects.filter(name__regex=r'^.*Atlantic.*$')
	# }
	# 7. all teams based in Dallas
	# context = {
	# 	'teams': Team.objects.filter(location="Dallas")
	# }
	# 8. all teams named the Raptors
	# context = {
	# 	'teams': Team.objects.filter(team_name='Raptors')
	# }
	# 9. all teams whose location includes "City"
	# context = {
	# 	'teams': Team.objects.filter(location__regex=r'^.*City.*$')
	# }
	# 10. all teams whose names begin with "T"
	# context = {
	# 	'teams': Team.objects.filter(team_name__istartswith='t')
	# }
	# 11. .all teams, ordered alphabetically by location
	# context = {
	# 	'teams': Team.objects.order_by('location')
	# }
	# 12. ...all teams, ordered by team name in reverse alphabetical order
	# context = {
	# 	'teams': Team.objects.order_by('-team_name')
	# }
	# 13. .every player with last name "Cooper"
	# context = {
	# 	'players': Player.objects.filter(last_name='Cooper')
	# }
	# 14. every player with first name "Joshua"
	# context = {
	# 	'players': Player.objects.filter(first_name='Joshua')
	# }
	# 15. every player with last name "Cooper" EXCEPT FOR Joshua
	# context = {
	# 	'players': Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua")
	# }
	# 16.all players with first name "Alexander" OR first name "Wyatt"
	# context = {
	# 	'players': Player.objects.filter(first_name='Alexander')|Player.objects.filter(first_name='Wyatt')
	# }


	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
