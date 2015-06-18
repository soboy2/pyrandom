from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017/')

player = {
    "name": "sho"
}

db = client.ff

def add():
    for player in players:
        db.players.insert(player)
    num_players = db.players.find().count()
    print "number of players added", num_players

def find():
    projection = {"_id": 0, "name": 1} #to limit what results to see
    query = {"position" : "wr", "avgPts" : {"$gte": 12}} #$regex
    players = db.players.find(query, projection)
    for player in players:
        pprint.pprint player


if _name_ == '_main_':
    find()
