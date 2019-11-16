import requests
from bs4 import BeautifulSoup
import openpyxl

# 엑셀은 comma를 신경쓰지 않아도 됨
# 엑셀 워크북 생성
wb = openpyxl.Workbook()
sheet = wb.active    # 현재 활성화된 sheet

header = ['제목', '채널명', '재생수', '좋아요수']
sheet.append(header)

raw = requests.get('https://tv.naver.com/r/', headers={'User-Agent':'Mozilla/5.0'})
code = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 : dl.cds_info
container = code.select('dl.cds_info')

# 태그를 포함한 데이터를 .text로 content부분만 가져온다.
for cont in container[:50]:
    # 제목 : dt.title
    title = cont.select_one('dt.title').text.strip()
    # 채널명 : dd.chn
    chn = cont.select_one('dd.chn').text.strip()
    # replace하거나 슬라이싱
    # 재생수 : span.hit
    hit = cont.select_one('span.hit').text.strip().replace(',', '').replace('재생 수', '')
    # 좋아요 : span.like
    like = cont.select_one('span.like').text.strip().replace(',', '').replace('좋아요 수', '')

    print(title, chn, hit, like)
    # 엑셀에서는 string으로 인식하기 때문에 int로 변환해주어야 한다.
    sheet.append([title, chn, int(hit), int(like)])

wb.save('navercast_top100.xlsx')