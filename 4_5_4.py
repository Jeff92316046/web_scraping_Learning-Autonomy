import requests
from bs4 import BeautifulSoup


def main():
    url = ('https://zh.wikipedia.org/wiki/%E6%B2%83%E5%B0%94%E5%A4%AB%E5%86%88%C2%B7%E9%98%BF%E9%A9%AC%E5%BE%B7%E4%B9%8C%E6%96%AF%C2%B7%E8%8E%AB%E6%89%8E%E7%89%B9')
    text = get_text(url, 'h1')
    for title in text:
        try:
            print(title.a.text.strip())
        except:
            break


def get_text(url, tag):
    try:
        get_url = requests.get(url)
        if get_url.status_code == 200:
            soup = BeautifulSoup(get_url.text, 'html.parser')
            return soup.find_all('li')
    except Exception as e:
        print('Exception : %s' % (e))
    return None


if __name__ == '__main__':
    main()
