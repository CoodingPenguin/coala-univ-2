from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

# 드라이버를 켜서 이 페이지로 접속
driver.get('https://nid.naver.com/')

# 아이디 입력하기
id_box = driver.find_element_by_css_selector('input#id')
id_box.send_keys('id')

# 비밀번호 입력하기
pw_box = driver.find_element_by_css_selector('input#pw')
pw_box.send_keys('password')

# 로그인 버튼 누르기
driver.find_element_by_css_selector('input.btn_global').click()