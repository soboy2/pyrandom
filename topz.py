from pymongo import MongoClient
import sys

client = MongoClient('mongodb://localhost:27017/')
db = client.fantasypros

def findTop(position, mean):
    print(mean)
    projection = {"_id": 0, "coeff_var": 1, "mean": 1, "name": 1}
    query = {"position": position,  "coeff_var":{"$gte":"", "$lte": "0.60"}, "mean":{"$gte": mean}}
    players = db.players.find(query, projection).sort([("coeff_var", 1)]).limit(25)
    for player in players:
        if float(player["mean"]) > float(mean):
            print(player["name"] + " " + player["mean"] + " " + player["coeff_var"])




if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        print('usage: [--position] [--avg]')
        sys.exit(1)

    if len(sys.argv) > 2:
        mean = args[1]
    else:
        mean = '12'

    pos = args[0]

    findTop(pos, mean)
