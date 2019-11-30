from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

# 드라이버를 켜서 이 페이지로 접속
driver.get('https://www.facebook.com/')

# 아이디 입력하기
id_box = driver.find_element_by_css_selector('input#email')
id_box.send_keys('id')

# 비밀번호 입력하기
pw_box = driver.find_element_by_css_selector('input#pass')
pw_box.send_keys('password')

# 로그인 버튼 누르기
driver.find_element_by_css_selector('input#u_0_e').click()