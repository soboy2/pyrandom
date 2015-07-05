from pymongo import MongoClient
from bs4 import BeautifulSoup
import json

client = MongoClient('mongodb://localhost:27017/')
db = client.fantasypros




def extract_data(page, yr):
    with open(page, 'rU') as html:
        #text = html.read()
        soup = BeautifulSoup(html.read())
        table = soup.find('table', attrs={'id':'data'})
        table_head = table.find('thead')
        headers = table_head.findAll('th')
        #for header in headers:
            #print header.string

        table_body = table.find('tbody')

        rows = table_body.findAll('tr')

        for row in rows:
            player_dict = {}
            cells = row.findAll('td')
            player_dict['rank'] = str(cells[0].find(text=True))
            player_dict['name'] = str(cells[1].find(text=True))
            player_dict['team'] = str(cells[2].find(text=True))
            player_dict['position'] = str(cells[3].find(text=True))
            player_dict['total_points'] = float(cells[4].find(text=True))
            player_dict['num_games_played'] = str(cells[5].find(text=True))
            player_dict['season_avg_points'] = float(cells[6].find(text=True))
            player_dict['season'] = str(yr)
            #insert player in db
            add_player(player_dict)
            print player_dict

def add_player(player):
    db.leaders.insert(player)

if __name__ == '__main__':
    for yr in range(2012, 2015):
        html_page = "fbhtml/fantasy_fb_leaders_" + str(yr) + ".html"
        extract_data(html_page, yr)
