import requests
from bs4 import BeautifulSoup

f = open('navernews.csv', 'w')
f.write('기사명,언론사명\n')

raw = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=오마이걸', headers={'User-Agent':'Mozilla/5.0'})
code = BeautifulSoup(raw.text, 'html.parser')

container = code.select('ul.type01 > li')

for cont in container:
    # 기사명
    title = cont.select_one('a._sp_each_title').text.strip().replace(',', '')
    # 언론사명
    writer = cont.select_one('span._sp_each_source').text.strip().replace(',', '')

    print(title, writer)
    f.write(title + ',' + writer + '\n')

f.close()