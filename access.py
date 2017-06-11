from ohmysportsfeedspy import MySportsFeeds
from api_access import username, password

from mongo_fns import mongoimport, mongoread, mongoremove

# To comment a line out simply start line with "#"

# Comment out  all three lines \/\/\/ when reading from mongo
Data_query = MySportsFeeds('1.0',verbose=True)
Data_query.authenticate(username, password)
Output = Data_query.msf_get_data(league='nhl',team='cbj',season='2016-2017-regular',format='json', feed='team_gamelogs')

# I comment \/\/\/ this out typically. Just distracting
# print(Output)

# Comment out \/\/\/ if you have data inserted and only want to read
Data_dbImport = mongoimport(Output)

# Comment out \/\/\/ if you want to read newly insert data
Data_dbRead = mongoread()

# Comment out \/\/\/ if you dont want to delete data
Data_Remove = mongoremove()
