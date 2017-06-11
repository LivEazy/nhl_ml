from pymongo import MongoClient

def mongoimport(data):
    client = MongoClient('localhost', 27017)
    db = client.nhl_ml
    coll = db.first_test
    insert = coll.insert_one(data)
    print "Data imported into mongodb 'nhl_ml' collection with ID of {}".format(insert.inserted_id)

def mongoread():
    client = MongoClient('localhost', 27017)
    db = client.nhl_ml
    coll = db.first_test
    cursor = coll.find({"teamgamelogs.gamelogs.game.homeTeam.Abbreviation": "CBJ"})
    for document in cursor:
        print(document)

def mongoremove():
    client = MongoClient('localhost', 27017)
    db = client.nhl_ml
    coll = db.first_test
    delete = coll.remove({})
    print(delete)
