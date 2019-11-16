from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')

# 드라이버를 켜서 이 페이지로 접속
driver.get('https://papago.naver.com/?sk=auto&tk=ko')

time.sleep(3)

# 단어 입력하기
input_box = driver.find_element_by_css_selector('textarea#txtSource')
input_box.send_keys('seize the day.')

# # 번역 버튼 누르기
# translate_button = driver.find_element_by_css_selector('button#btnTranslate')
# translate_button.click()

# 1초 delay
time.sleep(1)

result = driver.find_element_by_css_selector('div#txtTarget>span').text

print(result)
# 크롭 웹페이지를 닫음
driver.close()