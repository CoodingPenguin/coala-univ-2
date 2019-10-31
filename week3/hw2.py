import requests
from bs4 import BeautifulSoup

for page in range(1, 4):
    url = 'https://search.daum.net/search?w=news&q=오마이걸&DA=PGD&spacing=0&p='+str(page)
    raw = requests.get(url)

    code = BeautifulSoup(raw.text, 'html.parser')

    container = code.select('div.wrap_cont')

    for article in container:
        title = article.select_one('div.mg_tit').text.strip()
        content = article.select_one('p').text.strip()

        print('[{0}]\n{1}'.format(title, content))

    print('='*160)