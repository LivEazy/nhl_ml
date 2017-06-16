from ohmysportsfeedspy import MySportsFeeds
from api_access import username, password
import json
from playerlog_fns import playerlog_apipull, data

import pprint
pp = pprint.PrettyPrinter(indent=4)
playerlog = []
dataedit = data["playergamelogs"]["gamelogs"]
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



pp.pprint(playerlog)
