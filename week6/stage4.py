# 네이버 지도 데이터 수집하기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://map.naver.com/v5/search")

# 팝업 창 제거
driver.find_element_by_css_selector("button#intro_popup_close").click()

# 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector("div.input_box>input.input_search")
search_box.send_keys('마라탕')

# 검색버튼 누르기
search_box.send_keys(Keys.ENTER)

# 크롤링
for p in range(20):
    # 5초 delay
    time.sleep(5)

    # 데이터 확인하기
    stores = driver.find_elements_by_css_selector('div.list_search div.search_box')

    for s in stores:
        # 가게 이름
        name = s.find_element_by_css_selector('span.search_title_text').text
        # 가게 주소
        addr = s.find_element_by_css_selector('span.address').text
        # 가게 번호
        try:
            tel = s.find_element_by_css_selector('span.phone').text
        except:
            tel = 'None'
        print(name, addr, tel, sep='|')

    # 다음 페이지로 이동
    try:
        next_btn = driver.find_element_by_css_selector('button.btn_next')
        next_btn.click()
    except:
        print('데이터 수집 완료')
        break

# 크롭 웹페이지를 닫음
driver.close()