from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')

# 드라이버를 켜서 이 페이지로 접속
driver.get('https://www.instagram.com/explore/tags/ootd/')

# 현재 페이지에서 모든 사진들의 링크를 담은 리스트
link_list = [x.get_attribute('href') for x in driver.find_elements_by_css_selector('article div a')]
print(len(link_list))

for p in range(12):
    driver.get(link_list[p])

    print('[{}]'.format(p+1))
    # 본문 및 댓글
    try:
        post_comment = driver.find_elements_by_css_selector('article div li div>span')
        print(post_comment[1].text)
    except:
        post_comment = driver.find_element_by_css_selector('article>div>div>ul>div>li span')
        print(post_comment.text)

    print('='*100)

    time.sleep(1)