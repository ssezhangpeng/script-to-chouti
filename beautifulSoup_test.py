from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

browser = webdriver.Chrome()
url = "https://dig.chouti.com/"
browser.get(url)
html = browser.page_source

# label = browser.find_element_by_id('txtSearch2')
# search = browser.find_element_by_id('searchBtn_3')

# soup = BeautifulSoup(html,'lxml')
# ref_lists = soup.find_all(attrs={'class':'article-header'})
# contents = soup.select('.article-header h1')
# for content in contents:
#     print(content.get_text())

# label.send_keys("ipad")
# search.click()

# time.sleep(2)
# print(label.get_attribute('a'))
# ======登录=========
login = browser.find_element_by_id('login-link-a')  # 加载登录框
login.click()
time.sleep(1)

mobil = browser.find_element_by_id('mobile')
pwd = browser.find_element_by_id('mbpwd')
mobil.send_keys("18362758535")
pwd.send_keys("woshiniba")

time.sleep(2)

login = browser.find_element_by_class_name('btn-login')
login.click()

time.sleep(2)
# ======点赞=========
# ups = browser.find_elements_by_class_name('digg-a')
ups = browser.find_elements_by_css_selector('.digg-a b')
ups[0].click()
ups[2].click()
# for up in ups:
#     print(up.text)
time.sleep(2)
#===========退出操作=======
menu = browser.find_element_by_css_selector('#userProNick')
actions = ActionChains(browser)
actions.move_to_element(menu)
actions.perform()

time.sleep(1)
browser.find_element_by_css_selector('.logout').click()

time.sleep(2)
browser.close()
