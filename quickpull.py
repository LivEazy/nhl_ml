from ohmysportsfeedspy import MySportsFeeds
from api_access import username, password
import json
from playerlog_fns import playerlog_apipull, data

Data_query = MySportsFeeds('1.0',verbose=True)
Data_query.authenticate(username, password)
playergamelog= Data_query.msf_get_data(league='nhl', season='2016-2017-regular', feed='player_gamelogs',format='json', team = 'cbj', player = 'zach-werenski,cam-atkinson',limit = '100')
