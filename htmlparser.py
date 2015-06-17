from bs4 import BeautifulSoup

#r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
#r.status_code
#r.headers['content-type']
#r.text
#r.json()

s = requests.Session()


r = s.get("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2")

soup = BeautifulSoup(r.text)
