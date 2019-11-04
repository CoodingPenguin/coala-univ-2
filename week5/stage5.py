import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

url = 'https://movie.naver.com/movie/running/current.nhn'

raw = requests.get(url)
code = BeautifulSoup(raw.text, 'html.parser')

movies = code.select('dl.lst_dsc')

for m in movies:
    title = m.select_one('dt.tit>a').text.strip()
    score = m.select_one('div.star_t1 span.num').text.strip()

    print(title, score, sep='\n')

    # 리뷰가 있는 영화 상세페이지 크롤링
    link = m.select_one('dt.tit a').attrs["href"]
    link_to = 'https://movie.naver.com' + link

    raw2 = requests.get(link_to)
    code2 = BeautifulSoup(raw2.text, 'html.parser')

    img = code2.select_one('div.poster img')
    img_url = img.attrs['src']
    urlretrieve(img_url, './img/'+title[:2]+'.jpg')

    reviews = code2.select('div.score_result ul li')
    for r in reviews:
        star = r.select_one('div.star_score').text.strip()
        content = r.select_one('div.score_reple p').text.strip()
        print(star, content)

    print('='*100)