import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

url = 'https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth'
raw = requests.get(url)
code = BeautifulSoup(raw.text, 'html.parser')

movies = code.select('div.list_item')

special_key = input('Enter a genre of the movie you are finding : ')
for m in movies:
    # 제목
    title = m.select_one('h4').text
    # 메타스코어
    try:
        score = m.select_one('span.metascore').text.strip()
    except:
        score = 'None'

    # print(title, score)
    info = m.select('div.txt-block')

    # 장르
    cert_runtime = m.select('p span')
    genres = []
    for cr in cert_runtime:
        if cr.text == '15' or cr.text == '12' or cr.text == '|':
            continue
        genres.append(cr.text)

    # 감독
    directors_tag = info[0].select('a')
    directors = []
    for d in directors_tag:
        directors.append(d.text.strip())

    # 배우
    actors_tag = info[1].select('a')
    actors = []
    for a in actors_tag:
        actors.append(a.text.strip())

    # 이미지
    link = m.select_one('div.image>a').attrs["href"]
    link_to = 'https://www.imdb.com' + link

    raw2 = requests.get(link_to)
    code2 = BeautifulSoup(raw2.text, 'html.parser')

    # 이미지 추출
    img = code2.select_one('div.poster img')
    img_url = img.attrs['src']
    urlretrieve(img_url, './poster/'+title[:8]+'.jpg')

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