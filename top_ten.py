import nfldb

db = nfldb.connect()
q = nfldb.Query(db)

q.game(season_year=2015, season_type='Regular', team='OAK')
for game in q.as_games():
	print game
	
# for pp in q.sort('passing_yds').limit(10).as_aggregate():
# 	print pp.player, pp.passing_yds