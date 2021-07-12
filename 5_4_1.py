from bs4 import BeautifulSoup
import json
import requests
URL = "https://www.agefans.cc/catalog/all-all-all-all-all-time-"
dicts = {}
for times in range(127):
    print("page{}scraping".format(times+1))
    resp = requests.get(URL+"{}".format(times+1)).text
    soup = BeautifulSoup(resp, 'html5lib')
    divs = soup.find_all(class_='cell blockdiff2')
    for div in divs:
        name = div.find(class_="cell_imform_name").text
        author = div.find_all(class_="cell_imform_value")[5].text
        date = div.find_all(class_="cell_imform_value")[3].text
        dicts[name] = (author, date)

file = '5_27_1.json'
with open(file, 'w', encoding='utf-8') as obj:
    json.dump(dicts, obj, ensure_ascii=False, sort_keys=True, indent=2)
