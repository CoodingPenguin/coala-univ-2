import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

url = 'http://ticket2.movie.daum.net/Movie/MovieRankList.aspx'

raw = requests.get(url)
code = BeautifulSoup(raw.text, 'html.parser')

movies = code.select('ul.list_boxthumb>li')

for m in movies:
    # 영화 페이지 링크
    link = m.select_one('a.link_g').attrs["href"]

    raw2 = requests.get(link)
    code2 = BeautifulSoup(raw2.text, 'html.parser')

    # 컨테이너
    cont = code2.select_one('div.movie_summary')

    # 제목
    title = cont.select_one('strong.tit_movie').text.strip()

    # 평점
    score = cont.select_one('em.emph_grade').text.strip()

    # 장르
    genre_release = cont.select('dl.list_movie dd')
    genres = genre_release[0].text.strip().split('/')

    director_star = cont.select('dl.list_movie dd.type_ellipsis')

    # 감독
    director = director_star[0].select_one('a').text.strip()

    # 배우
    try:
        stars_tag = director_star[1].select('a.link_person')
        stars = [x.text.strip() for x in stars_tag]
    except:
        stars = None

    ########## 출력 ##########
    print('제목 :', title)
    print('평점 :', score)
    print('장르 :', genres)
    print('감독 :', director)
    print('배우 :', stars)
    print('='*100)
    #########################