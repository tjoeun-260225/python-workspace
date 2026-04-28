'''
방법 2가지 존재
1 : requests + BeautifulSoup

2 : newspaper3k 뉴스 수집 전용 라이브러리 로 수집하는 방법
pip install newspaper3k
'''
import requests
from bs4 import  BeautifulSoup

def 방법1번():
    주소 = "https://v.daum.net/v/20260428091147574"

    # 기계가 아니라 사람이 브라우저 접근한 척
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
    }

    웹사이트_응답 = requests.get(주소, headers=headers)
    soup = BeautifulSoup(웹사이트_응답.text, "html.parser")

    # 제목
    title = soup.find("h3", class_="tit_view")
    print("제목 : ", title.text if title else "못찾음")

    # 본문
    content = soup.find("div", class_="article_view")
    print("내용 : ", content.text.strip() if content else "못찾음")

    # 기자 이름 & 이메일
    reporter = soup.find("span", class_="info_reporter")
    print("기자 : ", reporter.text if reporter else "못찾음")

방법1번()