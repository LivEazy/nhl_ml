from ohmysportsfeedspy import MySportsFeeds
from api_access import username, password

def playerlog_apipull(team):
    Data_query = MySportsFeeds('1.0',verbose=True)
    Data_query.authenticate(username, password)
    playergamelog= Data_query.msf_get_data(league='nhl', season='2016-2017-regular', feed='player_gamelogs',format='json', team = team, limit = '5')
    return playergamelog

def playerlog_reformat(data):
    playerlog = []
    dataedit = data['playergamelogs']['gamelogs']
    x = 0
    for i in range(0,len(dataedit)):
        playerID = dataedit[i]["player"]["ID"]
        if not any(p.get('player',{}).get('ID',{}) == playerID for p in playerlog):
            playerlog.append({})
            playerlog[x]["player"] = dataedit[i]["player"]
            x+=1
        gameID = dataedit[i]["game"]["id"]
        playerlog[x-1]["player"]["game" + gameID] = dataedit[i]["game"]
        playerlog[x-1]["player"]["game" + gameID]["stats"] = dataedit[i]["stats"]
        playerlog[x-1]["player"]["game" + gameID]["team"] = dataedit[i]["team"]
    return playerlog
