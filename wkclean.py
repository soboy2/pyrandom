from pymongo import MongoClient
from bs4 import BeautifulSoup
import json

client = MongoClient('mongodb://localhost:27017/')
db = client.fantasypros




def extract_data(page, yr, wk):
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
            player_dict['week'] = str(wk)
            player_dict['season'] = str(yr)
            #insert player in db
            add_player(player_dict)
            print player_dict

def add_player(player):
    db.playersbywk.insert(player)

if __name__ == '__main__':
    for yr in range(2012, 2015):
        for wk in range(1, 18):
            html_page = "fbhtml/fantasy_fb_stats_" + str(yr) + "_wk" + str(wk) + ".html"
            extract_data(html_page, yr, wk)
