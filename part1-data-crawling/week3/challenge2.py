import requests
from bs4 import BeautifulSoup

for page in range(1, 4):
    url = 'http://news.ycombinator.com/news?p=' + str(page)
    raw = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})

    code = BeautifulSoup(raw.text, 'html.parser')

    articles = code.select('tr.athing')

    for article in articles:
        rank = article.select_one('span.rank').text
        title = article.select_one('a.storylink').text

        print('{0} {1}'.format(rank, title))