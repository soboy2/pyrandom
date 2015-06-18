from bs4 import BeautifulSoup
import requests

s = requests.Session()

for wk in range(1, 18):
    r = s.get("http://www.fantasypros.com/nfl/reports/leaders/ppr.php?year=2014&week=" + str(wk), auth=('user', 'pwd'))
    week_html = "fantasy_fb_leaders_wk" + str(wk) + ".html"
    f = open(week_html, "w")
    f.write(r.text)
