import requests
from bs4 import BeautifulSoup
import openpyxl

try:
    wb = openpyxl.load_workbook('naver_ebook.xlsx')
    sheet = wb.active
except:
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(['순위', '제목', '저자'])

for page in range(1, 4):
    url = 'https://search.daum.net/search?w=news&q=오마이걸&DA=PGD&spacing=0&p='+str(page)
    raw = requests.get(url)

    code = BeautifulSoup(raw.text, 'html.parser')

    container = code.select('div.wrap_cont')

    for article in container:
        title = article.select_one('div.mg_tit').text.strip().replace(',', '')
        content = article.select_one('p').text.strip().replace(',', '')

        print('[{0}]\n{1}'.format(title, content))
        f.write(title+','+content+'\n')

    print('='*160)

f.close()