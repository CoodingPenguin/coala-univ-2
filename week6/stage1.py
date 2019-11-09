# 정적 페이지 vs 동적 페이지
# 셀레니움 : 파이썬을 크롬창을 켜서 제어하는 것과 같은 것
import requests
from bs4 import BeautifulSoup

raw = requests.get('https://v4.map.naver.com/', headers={'User-Agent' : 'Mozilla/5.0'})
code = BeautifulSoup(raw.text, 'html.parser')

# 동적 페이지라서 안 됨
# 컨테이너 수집
stores = code.select('dl.lsnx det')
for s in stores:
    name = s.select_one('dt > a').text
    addr = s.select_one('dd.addr').text
    tel = s.select_one('dd.tel').text

    print(name, addr, tel)