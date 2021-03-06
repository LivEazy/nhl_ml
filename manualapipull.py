from ohmysportsfeedspy import MySportsFeeds
from api_access import username, password
import json
from playerlog_fns import playerlog_apipull, playerlog_reformat
from mongo_fns import mongoimport, mongoread, mongoremove, mongounwind


# Comment out  all three lines \/\/\/ when reading from mongo
# Data_query = MySportsFeeds('1.0',verbose=True)
# Data_query.authenticate(username, password)

#Example: #Data_query.msf_get_data(league='nba',season='2016-2017-regular',feed='player_gamelogs',format='json',player='stephen-curry')

##API Documentation: https://www.mysportsfeeds.com/data-feeds/api-docs/

# playergamelog= Data_query.msf_get_data(league='nhl', season='2016-2017-regular', feed='player_gamelogs',format='json', team = 'cbj', player = 'zach-werenski, cam-atkinson', limit = '100')
# playergamelog = playergamelog["playergamelogs"]
#teamgamelog = Data_query.msf_get_data(league='nhl',season='2016-2017-regular',feed='team_gamelogs', format='json')

#draftking = Data_query.msf_get_data(league='nhl',season='2016-2017-regular', feed='daily_dfs', format='json', team = 'cbj',player='zach-werenski')

# I comment \/\/\/ this out typically. Just distracting
#print(json.dumps(playergamelog, indent=4))
#print(json.dumps(teamgamelog, indent=4))
#print(json.dumps(draftking, indent=4))

# Comment out \/\/\/ if you have data inserted and only want to read
# Data_dbImport = mongoimport(playergamelog)

# Comment out \/\/\/ if you want to read newly insert data
Data_dbRead = mongounwind()

# Comment out \/\/\/ if you dont want to delete data
#Data_Remove = mongoremove()

#To pull player logs for teams
# teamnames = ['cbj','det']

# playerlogoutput = []
# for team in teamnames:
#     data = playerlog_apipull(team)
#     reformat = playerlog_reformat(data)
#     playerlogoutput += reformat
#
# with open('playerlogoutput', 'w') as fout:
#     json.dump(playerlogoutput, fout)
