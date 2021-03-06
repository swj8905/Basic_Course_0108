from selenium import webdriver
import time
from chromedriver_autoinstaller import install

browser = webdriver.Chrome(install())
browser.implicitly_wait(5)
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")
id = browser.find_element_by_css_selector("#id")
id.send_keys("talingpython")
pw = browser.find_element_by_css_selector("#inputPwd")
pw.send_keys("q1w2e3!@#")
browser.find_element_by_css_selector("#loginBtn").click()
time.sleep(3)
browser.get("http://cafe.daum.net/talingpython")
time.sleep(2)
# 중고나라 게시판 클릭
browser.switch_to.frame("down")
browser.find_element_by_css_selector("#fldlink_rRa6_347").click()
time.sleep(2)

try:
    f = open("./중고나라.txt", "r")
    ref = f.readlines()
except:
    f = open("./중고나라.txt", "w")
    ref = []
f.close()

title = browser.find_elements_by_css_selector("a.txt_item")
new_one = 0
for i in title:
    if (i.text+"\n") not in ref: # i.text가 최신 글이라면?
        f = open("./중고나라.txt", "a")
        f.write(i.text + "\n")
        f.close()
        if "모니터" in i.text:
            new_one += 1
print(f"모니터 관련 글이 {new_one}개 올라왔습니다.")
browser.close()

if new_one >= 1:
    from twilio.rest import Client

    account_sid = "ACe0ac1409ef60e797a66800a73c0908be"
    auth_token = "3fc9e78ea9b5bd6989fd0bf5a00682c7"
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=f"모니터 관련 글이 {new_one}개 올라왔습니다. https://cafe.daum.net/talingpython/rRa6",
                         from_='+19205573964',
                         to='+821095518905'
                     )