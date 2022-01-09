from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par

keyword = input("키워드 입력 >> ")
encoded = par.quote(keyword) # 한글 --> 특수한 문자열

page_num = 1
while True:
    url = f"https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Used&KeyWord={encoded}&KeyRecentPublish=0&OutStock=0&ViewType=Detail&SortOrder=11&CustReviewCount=0&CustReviewRank=0&KeyFullWord={encoded}&KeyLastWord={encoded}&CategorySearch=&chkKeyTitle=&chkKeyAuthor=&chkKeyPublisher=&ViewRowCount=25&page={page_num}"
    code = req.urlopen(url)
    soup = BeautifulSoup(code, "html.parser")
    title = soup.select("a.bo3 > b")
    if len(title) == 0: # 크롤링 다 했다면?
        print("======== 크롤링 끝! ==========")
        break
    for i in title:
        print(i.text)
    page_num += 1