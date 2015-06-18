from bs4 import BeautifulSoup
import requests

#r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
#r.status_code
#r.headers['content-type']
#r.text
#r.json()

s = requests.Session()

for yr in range(2010, 2015):
    r = s.get("http://www.fantasypros.com/nfl/reports/leaders/ppr.php?year=" + str(yr), auth=('user', 'pwd'))
    f = open("fantasy_fb_leaders_" + str(yr) + ".html", "w")
    f.write(r.text)



#soup = BeautifulSoup(r.text)
