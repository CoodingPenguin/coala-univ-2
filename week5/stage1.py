import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/running/current.nhn'

raw = requests.get(url)
code = BeautifulSoup(raw.text, 'html.parser')

movies = code.select('dl.lst_dsc')

for m in movies:
    title = m.select_one('dt.tit>a').text.strip()
    score = m.select_one('div.star_t1 span.num').text.strip()

    # 8.5보다 낮으면 skip
    if float(score) < 8.5:
        continue

    print(title, score, sep='\n')
    # 선택자가 같은 경우
    # 방법 1 : 리스트 인덱싱
    info = m.select('dl.info_txt1 dd')

    genre = info[0].select('a')
    print('장르 :')
    for g in genre:
        print(g.text.strip())

    directors = info[1].select('a')
    print('감독 :')
    for d in directors:
        print(d.text.strip())

    try:
        actors = info[2].select('a')
        print('배우 :')
        for a in actors:
            print(a.text.strip())
    except:
        print('None')

    print('='*100)