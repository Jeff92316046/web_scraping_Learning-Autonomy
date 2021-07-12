import requests
from bs4 import BeautifulSoup
import url
resp = requests.get(url.data1)
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup.find('h1').text)
