import requests
from bs4 import BeautifulSoup

for page in range(1, 6):
    url = 'https://series.naver.com/ebook/top100List.nhn?page='+str(page)
    raw = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    code = BeautifulSoup(raw.text, 'html.parser')

    container = code.select('ul.lst_thum>li')

    for book in container:
        rank = book.select_one('span.num').text
        title = book.select_one('a>strong').text
        author = book.select_one('span.writer').text

        print('{0}위: {1}의 {2}'.format(rank, author, title))