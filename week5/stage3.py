# 어떤 조건을 만족하는 데이터만 추출
import requests
from bs4 import BeautifulSoup

# 크롤링할 사이트 주소
url = 'https://movie.naver.com/movie/running/current.nhn'

# 크롤링 + html로 변환
raw = requests.get(url)
code = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너
movies = code.select('dl.lst_dsc')

for m in movies:
    title = m.select_one('dt.tit>a').text.strip()                   # 제목
    score = m.select_one('div.star_t1 span.num').text.strip()       # 평점

    print(title, score, sep='\n')

    # 8.5보다 낮으면 skip
    if float(score) < 8.5:
        continue

    # 선택자가 같은 경우
    # 방법 2 : nth-of-type
    genre = m.select_one('dl.info_txt1 dd:nth-of-type(1)')
    if '액션' in genre.text:
        continue
    print('장르 :', genre.text)

    directors = m.select('dl.info_txt1 dd:nth-of-type(2) a')
    print('감독 :')
    for d in directors:
        print(d.text.strip())

    actors = m.select('dl.info_txt1 dd:nth-of-type(3) a')
    print('배우 :')
    try:
        for a in actors:
            print(a.text.strip())
    except:
        print('None')

    print('='*100)