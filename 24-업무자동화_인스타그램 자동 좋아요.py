from selenium import webdriver
from chromedriver_autoinstaller import install
import time

keyword = input("해시태그 검색 >> ")
browser = webdriver.Chrome(install())
browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
time.sleep(2)
# 로그인 하기
id = browser.find_element_by_name("username")
id.send_keys("tutor_pyson") # 본인 계정 적어주세요
pw = browser.find_element_by_name("password")
pw.send_keys("q1w2e3r4!@#$") # 본인 계정 적어주세요
button = browser.find_element_by_css_selector("div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB")
button.click()
time.sleep(5)
# 해시태그 검색
browser.get(f"https://www.instagram.com/explore/tags/{keyword}")
time.sleep(5)
# 첫번째 사진 클릭
first_photo = browser.find_element_by_css_selector("div._9AhH0")
first_photo.click()
time.sleep(4)
# 자동 좋아요 시작
while True:
    like = browser.find_element_by_css_selector("section.ltpMr.Slqrh span > svg._8-yf5")
    value = like.get_attribute("aria-label")
    next = browser.find_element_by_css_selector("div.l8mY4.feth3 > button.wpO6b")
    if value == "좋아요": # 좋아요가 안눌려있다면?
        like.click()
        time.sleep(30)
        next.click()
        time.sleep(30)
    else:
        next.click()
        time.sleep(30)