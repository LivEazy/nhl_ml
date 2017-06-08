from ohmysportsfeedspy import MySportsFeeds
from api_access import username, password

Data_query = MySportsFeeds('1.0',verbose=True)
Data_query.authenticate(username, password)
Output = Data_query.msf_get_data(league='nba',season='2016-2017-regular',feed='player_gamelogs',format='json',player='stephen-curry')

print(Output)
