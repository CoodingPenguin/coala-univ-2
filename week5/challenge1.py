# 특정 장르의 영화만 추출해내기
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth'
raw = requests.get(url)
code = BeautifulSoup(raw.text, 'html.parser')

movies = code.select('div.list_item td.overview-top')

# 특정 장르
special_key = input('Enter a genre of the movie you are finding : ')
for m in movies:
    ############# 데이터(제목, 메타스코어, 장르, 감독, 배우) #############
    # 제목
    title = m.select_one('h4').text
    # 메타스코어
    try:
        score = m.select_one('span.metascore').text.strip()
    except:
        score = 'None'

    # print(title, score)


    # 장르 (여러 개)
    cert_runtime = m.select('p span')   # 해당 태그 다 불러옮
    genres = []                         # 필요한 것들만 genres 리스트에 추가
    for cr in cert_runtime:
        if cr.text == '15' or cr.text == '12' or cr.text == '|':
            continue
        genres.append(cr.text)

    info = m.select('div.txt-block')

    # 감독 (여러 명)
    directors_tag = info[0].select('a')
    directors = []
    for d in directors_tag:
        directors.append(d.text.strip())

    # 배우 (여러 명)
    actors_tag = info[1].select('a')
    actors = []
    for a in actors_tag:
        actors.append(a.text.strip())

    # special_key가 genres에 있는 영화만 출력
    if special_key in genres:
        print('제목 :', title)
        print('평점 :', score)
        print('장르 :', end=' ')
        for g in genres:
            print(g, end=' ')
        print('\n감독 :', end=' ')
        for d in directors:
            print(g, end=' ')
        print('\n출연진 :', end=' ')
        for a in actors:
            print(a, end=' ')
        print()
        print('=' * 100)