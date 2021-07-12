import requests
import json
from bs4 import BeautifulSoup
URL = ('https://www.ptt.cc/bbs/Gossiping/index.html')
resp = requests.get(url=URL,
                    cookies={'over18': '1'}).text
soup = BeautifulSoup(resp, 'html5lib')
paging_div = soup.find('div', 'btn-group btn-group-paging')
prev_url = paging_div.find_all('a')[1]['href']
dicts = {}
divs = soup.find_all('div', 'r-ent')
for div in divs:
    name = div.find(class_='title').text.strip()
    author = div.find(class_='author').text.strip()
    date = div.find(class_='date').text.strip()
    dicts[name] = (author, date)
file = '4_17_2.json'
with open(file, 'w', encoding='utf-8') as obj:
    json.dump(dicts, obj, ensure_ascii=False, sort_keys=True, indent=2)
