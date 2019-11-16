from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')

# 드라이버를 켜서 이 페이지로 접속
driver.get('https://v4.map.naver.com')

# 팝업창 끄기
close_button = driver.find_elements_by_css_selector('button.btn_close')
close_button[1].click()

# 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector('input#search-input')
search_box.send_keys('강남 뷔페')

# 검색버튼 누르기
search_button = driver.find_element_by_css_selector('button.spm')
search_button.click()

# 1초 delay
time.sleep(1)

# 데이터 확인하기
stores = driver.find_elements_by_css_selector('div.lsnx')
for s in stores:
    # 가게 이름
    name = s.find_element_by_css_selector('dt > a').text
    # 가게 주소
    addr = s.find_element_by_css_selector('dd.addr').text
    # 가게 번호
    tel = s.find_element_by_css_selector('dd.tel').text

    print(name, addr, tel)

# 크롭 웹페이지를 닫음
driver.close()