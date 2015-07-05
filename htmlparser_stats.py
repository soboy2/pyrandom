from bs4 import BeautifulSoup
import requests

s = requests.Session()

for yr in range(2012, 2015):
    for wk in range(1, 18):
        r = s.get("http://www.fantasypros.com/nfl/reports/leaders/ppr.php?year="+ str(yr) + "&week=" + str(wk), auth=('usr', 'pwd'))
        week_html = "fantasy_fb_stats_" + str(yr) + "_wk" + str(wk) + ".html"
        f = open(week_html, "w")
        f.write(r.text)
