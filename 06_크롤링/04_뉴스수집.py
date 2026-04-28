'''
방법 2가지 존재
1 : requests + BeautifulSoup

2 : newspaper3k 뉴스 수집 전용 라이브러리 로 수집하는 방법
pip install newspaper3k
'''
import requests
from bs4 import BeautifulSoup


def 방법1번():
    주소 = "https://v.daum.net/v/20260428091147574"

    # 기계가 아니라 사람이 브라우저 접근한 척
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
    }

    웹사이트_응답 = requests.get(주소, headers=headers)
    soup = BeautifulSoup(웹사이트_응답.text, "html.parser")
    # soup = requests로 가져온 텍스트를 분해했고, 분해한 데이터가 들어있는 공간
    # 제목
    # 분해한 공간에서 하나의 데이터찾기
    #                html태그 class_ html 태그에서 클래스이름으로 작성되어 있는 태그
    title = soup.find("h3", class_="tit_view")
    print("제목 : ", title.text if title else "못찾음")

    # 본문
    content = soup.find("div", class_="article_view")
    print("내용 : ", content.text.strip() if content else "못찾음")

    # 기자 이름 & 이메일
    reporter = soup.find("span", class_="info_reporter")
    print("기자 : ", reporter.text if reporter else "못찾음")


# 방법1번()
# class 객체이름:

'''
newspaper3k 업데이트 중단되었음
from newspaper import Article 이러한 방식은 3k 버전에서 많이 사용

pip install newspaper4k lxml_html_clean
import newspaper 4k 버전에서는 import로 단순하게 사용
'''
from newspaper import Article

def newspaper3_Old_Version():
    주소 = "https://v.daum.net/v/20260428091147574"

    article = Article(주소, language="ko") #3k 구버전
    article.download()
    article.parse()

    print("제목 : ", article.title)
    print("내용 : ", article.text)
    print("기자 : ", article.authors)
    print("날짜 : ", article.publish_date)


import newspaper
import nltk
nltk.download('punkt_tab')
def newspaper4_New_Version():
    주소 = "https://v.daum.net/v/20260428091147574"

    article = newspaper.article(주소, language="ko")
    article.parse()

    print("제목 : ", article.title)
    print("내용 : ", article.text)
    print("기자 : ", article.authors)
    print("날짜 : ", article.publish_date)

newspaper4_New_Version()
