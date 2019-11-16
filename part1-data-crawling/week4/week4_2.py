import requests
from bs4 import BeautifulSoup

f = open('navercast_top100.csv', 'w')
f.write('제목,채널명,재생수,좋아요수\n')

raw = requests.get('https://tv.naver.com/r/', headers={'User-Agent':'Mozilla/5.0'})
code = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 : dl.cds_info
container = code.select('dl.cds_info')

# 태그를 포함한 데이터를 .text로 content부분만 가져온다.
for cont in container[:50]:
    # 제목 : dt.title
    title = cont.select_one('dt.title').text.strip().replace(',', '')
    # 채널명 : dd.chn
    chn = cont.select_one('dd.chn').text.strip().replace(',', '')
    # replace하거나 슬라이싱
    # 재생수 : span.hit
    hit = cont.select_one('span.hit').text.strip().replace(',', '').replace('재생 수', '')
    # 좋아요 : span.like
    like = cont.select_one('span.like').text.strip().replace(',', '')

    print(title, chn, hit, like)
    f.write(title+','+chn+ ',' + hit+','+like[5:]+'\n')

f.close()