from bs4 import BeautifulSoup
import json
import requests
URL = ('https://www.ptt.cc/bbs/Gossiping/index.html')
prev_url = 'bbs/Gossiping/index.html'
dicts = {}
for times in range(5):
    print("page{}scraping".format(times+1))
    resp = requests.get(url='https://www.ptt.cc/'+prev_url,
                        cookies={'over18': '1'}).text
    soup = BeautifulSoup(resp, 'html5lib')
    paging_div = soup.find('div', 'btn-group btn-group-paging')
    prev_url = paging_div.find_all('a')[1]['href']
    divs = soup.find_all('div', 'r-ent')
    for div in divs:
        name = div.find(class_='title').text.strip()
        author = div.find(class_='author').text.strip()
        date = div.find(class_='date').text.strip()
        dicts[name] = (author, date)
    resp = requests.get(url='https://www.ptt.cc/'+prev_url,
                        cookies={'over18': '1'}).text
    soup = BeautifulSoup(resp, 'html5lib')
file = '4_17_3.json'
with open(file, 'w', encoding='utf-8') as obj:
    json.dump(dicts, obj, ensure_ascii=False,
              indent=2)
