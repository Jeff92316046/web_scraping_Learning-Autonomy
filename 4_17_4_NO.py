import requests
import json
from bs4 import BeautifulSoup
URL = ('https://ldap.tp.edu.tw/login')
s = requests.session()

resp = s.get(URL)
soup = BeautifulSoup(resp.text, 'html5lib')
token = soup.find('div', class_="form-bottom").find('form',
                                                    {'data-stage': "DataStore1"}).find('input')['value']

# ['value'], type_="hidden"


print(token)
form = {
    '_token': token,
    'username': 'lssh10831037',
    'paseword': '029140'
}

resp = s.post(url=URL, data=form)
resp = s.get('https://sschool.tp.edu.tw/Index.action')
print(resp.status_code)
