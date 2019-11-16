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
search_box.send_keys('신촌 치킨')

# 검색버튼 누르기
search_button = driver.find_element_by_css_selector('button.spm')
search_button.click()

for p in range(1, 20):
    # 1초 delay
    time.sleep(1)

    # 데이터 확인하기
    stores = driver.find_elements_by_css_selector('dl.lsnx_det')
    for s in stores:
        # 가게 이름
        name = s.find_element_by_css_selector('dt > a').text
        # 가게 주소
        addr = s.find_element_by_css_selector('dd.addr').text
        # 가게 번호
        try:
            tel = s.find_element_by_css_selector('dd.tel').text
        except:
            tel = 'None'
        print(name, addr, tel)

    # 다음 페이지로 이동
    try:
        page_bar = driver.find_elements_by_css_selector('div.paginate > *')
        if p % 5 != 0:
            page_bar[p % 5 + 1].click()
        else:
            page_bar[6].click()
    except:
        print('데이터 수집 완료')
        break

# 크롭 웹페이지를 닫음
driver.close()