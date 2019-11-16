# 이미지 저장하는 법
from urllib.request import urlretrieve

img_url = 'https://i.ytimg.com/vi/H8VFoeJPd9g/maxresdefault.jpg'    # 이미지 주소
urlretrieve(img_url, './img/오마이걸.jpg')                          # img폴더에 이미지 저장