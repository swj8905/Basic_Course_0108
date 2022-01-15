from selenium import webdriver
from chromedriver_autoinstaller import install
import time

browser = webdriver.Chrome(install())
browser.get("https://www.chosun.com/nsearch/?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC")
title = browser.find_elements_by_css_selector("div.story-card__headline-container.\|.box--margin-bottom-xs > div > a > span")
for i in title:
    print(i.text)