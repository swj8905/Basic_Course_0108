from selenium import webdriver
from chromedriver_autoinstaller import install
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(install())
browser.implicitly_wait(10)
browser.get("https://www.youtube.com/watch?v=TNU6N54F4LE")
time.sleep(5)
browser.find_element_by_css_selector("html").send_keys(Keys.PAGE_DOWN) # PAGE_DOWN : 스크롤 살짝 / END : 스크롤 끝까지
time.sleep(5)
comments = browser.find_elements_by_css_selector("#content-text")
idx = 0
while True:
    try:
        print(comments[idx].text)
    except:
        print("======= 크롤링 끝! =======")
        break

    idx += 1
    if idx % 20 == 0: # idx 가 20의 배수라면?
        browser.find_element_by_css_selector("html").send_keys(Keys.END)  # PAGE_DOWN : 스크롤 살짝 / END : 스크롤 끝까지
        time.sleep(4)
        comments = browser.find_elements_by_css_selector("#content-text")
