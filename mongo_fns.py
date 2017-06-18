from pymongo import MongoClient

def mongoimport(data):
    client = MongoClient('localhost', 27017)
    db = client.nhl_ml
    coll = db.player_logs
    insert = coll.insert_one(data)
    print "Data imported into mongodb 'nhl_ml' collection with ID of {}".format(insert.inserted_id)

def mongoread():
    client = MongoClient('localhost', 27017)
    db = client.nhl_ml
    coll = db.player_logs
    cursor = coll.find({"gamelogs.player.LastName" : "Werenski"})
    for document in cursor:
        print(document)

def mongounwind():
    client = MongoClient('localhost', 27017)
    db = client.nhl_ml
    coll = db.player_logs
    cursor = coll.aggregate( [
    { "$unwind": "$gamelogs" }
    ] )
    for document in cursor:
        print(document)
        print()

def mongoremove():
    client = MongoClient('localhost', 27017)
    db = client.nhl_ml
    coll = db.first_test
    delete = coll.remove({})
    print(delete)
