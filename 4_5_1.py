import requests
from bs4 import BeautifulSoup
resp = requests.get(
    'https://zh.wikipedia.org/wiki/%E6%B2%83%E5%B0%94%E5%A4%AB%E5%86%88%C2%B7%E9%98%BF%E9%A9%AC%E5%BE%B7%E4%B9%8C%E6%96%AF%C2%B7%E8%8E%AB%E6%89%8E%E7%89%B9')
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup.find('h1').text)
