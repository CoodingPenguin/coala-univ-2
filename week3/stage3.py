import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?&where=news&query=오마이걸&sm=tab_tmr&frm=mr&nso=so:r,p:all,a:all&sort=0'
# python에서 웹페이지에 들어가서 코드를 긁어오는 것
# 네이버에서 데이터를 긁어오는 것을 막음
# 그래서 브라우저웹에서 들어오는 것처럼 위장
raw = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
code = BeautifulSoup(raw.text, 'html.parser')
# print(code)

# 컨테이너 : id로 특정해주지 않아도 됨
clips = code.select('ul.type01 > li')

for clip in clips:
    title = clip.select_one('a._sp_each_title').text
    chn = clip.select_one('span._sp_each_source').text

    print('제목 : {0}\n언론사명:{1}'.format(title, chn))
    print('='*80)