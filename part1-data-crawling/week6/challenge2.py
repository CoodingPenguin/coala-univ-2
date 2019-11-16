from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')

# 드라이버를 켜서 이 페이지로 접속
driver.get('https://www.google.com/maps/')

# 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector('input#searchboxinput')
search_box.send_keys('카페')

# 검색버튼 누르기
search_button = driver.find_element_by_css_selector('button#searchbox-searchbutton')
search_button.click()

for i in range(1, 20):
    # 1초 delay
    time.sleep(7)

    # 데이터 확인하기
    stores = driver.find_elements_by_css_selector('div.section-result-content')
    for s in stores:
        # 가게 이름
        name = s.find_element_by_css_selector('h3>span').text
        # 가게 주소
        addr = s.find_element_by_css_selector('div.section-result-details-container span.section-result-location').text
        # 가게 평점
        try:
            score = s.find_element_by_css_selector('span.cards-rating-score').text
        except:
            score = 'None'
        print(name, addr, score)

    # 다음 페이지로 이동
    page_bar = driver.find_element_by_css_selector('button#n7lv7yjyC35__section-pagination-button-next')
    page_bar.click()


# 크롭 웹페이지를 닫음
driver.close()