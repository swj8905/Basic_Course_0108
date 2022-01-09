from bs4 import BeautifulSoup
import urllib.request as req

# 서버로부터 HTML 코드 받아오기
code = req.urlopen("http://www.cgv.co.kr/movies/?lt=1&ft=0")
# print(code.read())

# HTML 코드 이쁘게 정리하기
soup = BeautifulSoup(code, "html.parser")
# print(soup)

# 내가 원하는 요소를 컴퓨터한테 알려주기
# title = soup.select_one("strong.title")
title = soup.select("strong.title")

# 요소의 내용 출력하기
# print(title.text) # .string 보다 .text를 쓰세요.
num = 1
for i in title:
    print(f"{num}위 : {i.text}")
    num += 1