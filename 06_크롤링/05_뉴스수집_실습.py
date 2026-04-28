# 뉴스를 보고 분석
import requests
import newspaper
from bs4 import BeautifulSoup

# 방법 1번을 사용
# https://n.news.naver.com/article/277/0005755604?ntype=RANKING
# 네이버 뉴스에서 제목 내용 기자 추출
url = "https://n.news.naver.com/article/277/0005755604?ntype=RANKING"


def 방법1번():
    # 기계가 아니라 사람이 브라우저 접근한 척
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
    }

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    제목 = soup.find("h2", id="title_area")
    print("제목 :", 제목.text.strip() if 제목 else "못 찾음")

    # div 태그로 id 가 dic_area 인 태그가 없다.
    # 내용 = soup.find("div", id="dic_area") <article id="dic_area" class="go_trans _article_content">
    내용 = soup.find("article", id="dic_area")
    print("내용 :", 내용.text.strip() if  내용 else "못 찾음")
    # "" html 태그이름 작성할 때 "" 사이에 띄어쓰기가 존재해서 안되며
    # id 나 class 명 "" 내부도 마찬가지로 띄어쓰기 작성해서는 안된다.
    기자 = soup.find("span", class_="byline_s")
    print("기자 :", 기자.text.strip() if  기자 else "못 찾음")
# 방법 2번을 사용
# https://n.news.naver.com/article/277/0005755604?ntype=RANKING
# 네이버 뉴스에서 제목 내용 기자 추출
# 방법1번()

'''
import newspaper
import nltk
nltk.download('punkt_tab')
nltk 안에 있는 punkt_tab 가져와서 설치하기를 최초1회 실행하고나면 매번 작성할 필요가 없다.

보통 뉴스들의 형식을 자동으로 nltk 분석해서 제공
newspaper 모듈에서 article기능 안에 punkt_tab 분석해서 제목 내용 날짜 기자 를 추출하는 기능이 들어있다.
'''

def 방법2번():
    아티클 = newspaper.article(url, language = "ko")
    아티클.parse()

    print("제목 : ", 아티클.title)
    print("내용 : ", 아티클.text)
    print("기자 : ", 아티클.authors)       # 한국의 기자와 날짜를 자동으로 못 읽는 현상
    print("날짜 : ", 아티클.publish_date) # BeautifulSoup 조합해서 사용

방법2번()