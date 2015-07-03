from pymongo import MongoClient
import pprint
import statistics

client = MongoClient('mongodb://localhost:27017/')
db = client.fantasypros

def find():
    players = db.playersbywk.distinct("name")
    for player in players:
        getstats(player)


def getstats(player):
    points = []
    player_position = ''
    projection = {"_id": 0, "total_points": 1, "position": 1}
    query = {'name': player}
    player_details = db.playersbywk.find(query, projection)
    for player_detail in player_details:
        points.append(player_detail['total_points'])
        player_position = player_detail['position']
    savestats(player, points, player_position)


def savestats(player, points, player_position):
    player_dict = {}
    player_dict['name'] = player
    print("Player: " + player)

    player_dict['position'] = player_position
    print("Position: " + player_position)

    player_dict['mean'] = str(statistics.mean(points))
    print("Mean is: " + str(statistics.mean(points)))

    if len(points) >= 2:
        player_dict['stdev'] = str(statistics.stdev(points))
        print("Standard Deviation is: " + str(statistics.stdev(points)))

    if statistics.mean(points) != 0 and len(points) >= 2:
        player_dict['coeff_var'] = str(statistics.stdev(points)/statistics.mean(points))
        print("Coefficient of Variance is: " + str(statistics.stdev(points)/statistics.mean(points)))

    print("Number of games: " + str(len(points)))
    player_dict['num_of_games'] = str(len(points))

    db.players.insert(player_dict)



if __name__ == '__main__':
    find()
