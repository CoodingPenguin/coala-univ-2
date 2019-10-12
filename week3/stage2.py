import requests
from bs4 import BeautifulSoup

raw = requests.get('http://tv.naver.com/r')       # 주소로 들어가서 데이터를 긁어와라
# print(raw)                                      # <Response [200]> : 잘 접속했다!

# print(raw.text)                                 # 소스코드 but, str형태이므로 가공을 할 수 없음
code = BeautifulSoup(raw.text, 'html.parser')     # str을 html코드로 바꿔준다
# print(code)

# 1위 - 3위
# 컨테이너 : div.inner
# select : 여러 개를 찾을 때
clips = code.select('div.inner')                   # div.inner 부분만 땜
# print(len(clips))                                # len으로 원하는 데이터 개수를 정확히 긁어왔는지 확인

# div.inner는 이미 선택되어 있으므로 그 하위 것을 선택
# select_one : 하나만 찾고 싶을 때
for clip in clips:
    # 제목 : div.inner dl.cds_info > dt.title
    title = clip.select_one('dt.title').text
    # 채널명 : div.inner dl.cds_info > dd.chn
    chn = clip.select_one('dd.chn').text
    # 재생수 : div.inner dl.cds_info span.hit
    hit = clip.select_one('span.hit').text
    # 좋아요 : div.inner dl.cds_info span.like
    like = clip.select_one('span.like').text

    print('제목 : {0}, 채널명 : {1}, 재생수 : {2}, 좋아요 : {3}'.format(title, chn, hit, like))
    print('='*40)