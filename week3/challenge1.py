import requests
from bs4 import BeautifulSoup

raw = requests.get('http://tv.naver.com/r')
code = BeautifulSoup(raw.text, 'html.parser')

# 4위 - 100위
clips_new = code.select('div.cds')
for clip in clips_new:
    # 제목 : dl.cds_info > dt.title
    title = clip.select_one('dt.title').text
    # 채널명 : dl.cds_info > dd.chn
    chn = clip.select_one('dd.chn').text
    # 재생수 : dl.cds_info span.hit
    hit = clip.select_one('span.hit').text
    # 좋아요 : dl.cds_info span.like
    like = clip.select_one('span.like').text

    print('제목 : {0}채널명 : {1}재생수 : {2}좋아요 : {3}'.format(title, chn, hit, like))
    print('='*80)