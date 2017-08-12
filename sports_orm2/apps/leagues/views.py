from django.shortcuts import render, redirect
from django.db.models import Count, Avg
from .models import League, Team, Player
import re
from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}
#1 ...all teams in the Atlantic Soccer Conference
	# context = {
	# 	'teams': Team.objects.filter(league__name='Atlantic Soccer Conference')
	# }
#2 ...all (current) players on the Boston Penguins
	# context={
	# 	'players': Player.objects.filter(curr_team__location="Boston", curr_team__team_name="Penguins"),
	# }
#3 ...all (current) players in the International Collegiate Baseball Conference
	# context = {
	# 	'players': Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
	# 	'teams': Team.objects.filter(league__name="International Collegiate Baseball Conference")
	# }
#4 ...all (current) players in the American Conference of Amateur Football with last name "Lopez"
	# context = {
	# 	'players': Player.objects.filter(last_name='Lopez', curr_team__league__name='American Conference of Amateur Football')
	# }
#5 ...all football players
	# context = {
	# 	'players': Player.objects.filter(curr_team__league__sport='Football')
	# }
#6 ...all teams with a (current) player named "Sophia"
	# context = {
	# 	'teams': Team.objects.filter(curr_players__first_name='Sophia')
	# }
#7 ...all leagues with a (current) player named "Sophia"
	# context = {
	# 	'leagues': League.objects.filter(teams__curr_players__first_name='Sophia')
	# }
#8 ...everyone with the last name "Flores" who DOESN'T (currently) play for the Washington Roughriders
	# context = {
	# 	'players': Player.objects.filter(last_name='Flores').exclude(curr_team__team_name="Roughriders", curr_team__location='Washington')
	# }
#9 ...all teams, past and present, that Samuel Evans has played with
	# context = {
	# 	'teams': Team.objects.filter(all_players__first_name="Samuel", all_players__last_name="Evans")
	# }
#10 ...all players, past and present, with the Manitoba Tiger-Cats
	# context = {
	# 	'players': Player.objects.filter(all_teams__team_name="Tiger-Cats", all_teams__location="Manitoba")
	# 	}
#11 ...all players who were formerly (but aren't currently) with the Wichita Vikings
	# context = {
	# 	'players': Player.objects.filter(all_teams__location="Wichita", all_teams__team_name='Vikings').exclude(curr_team__location="Wichita",curr_team__team_name="Vikings")
	# }
#12 ...every team that Jacob Gray played for before he joined the Oregon Colts
	# context = {
	# 	'teams': Team.objects.filter(all_players__first_name='Jacob', all_players__last_name='Gray').exclude(curr_players__first_name= 'Jacob', curr_players__last_name='Gray')
	# }
#13 ...everyone named "Joshua" who has ever played in the Atlantic Federation of Amateur Baseball Players
	# context = {
	# 	'players': Player.objects.filter(first_name='Joshua', all_teams__league__name="Atlantic Federation of Amateur Baseball Players" )
	# }
#14 ...all teams that have had 12 or more players, past and present. (HINT: Look up the Django annotate function.)
	# context = {
	# 	  	'teams': Team.objects.annotate(num_players=Count('all_players')).filter(num_players__gte=12)
	#
	# }
#15 ...all players, sorted by the number of teams they've played for
	# context = {
	# 	'players': Player.objects.annotate(num_teams=Count('all_teams')).order_by('num_teams')
	# }

	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
