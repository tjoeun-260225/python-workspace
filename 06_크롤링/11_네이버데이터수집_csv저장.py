# 05 번에 위치한 코드를 가져온 후
# 방법 1번은 requests이용한naver뉴스수집.csv 저장
# 방법 2번은 newspaper이용한naver뉴스수집.csv 저장
import pandas as pd
import requests
import newspaper
from bs4 import BeautifulSoup

url = "https://n.news.naver.com/article/277/0005755604?ntype=RANKING"


def 방법1번():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
    }
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    제목 = soup.find("h2", id="title_area")
    제목데이터 = 제목.text.strip() if 제목 else "못 찾음"
    내용 = soup.find("article", id="dic_area")
    내용데이터 = 내용.text.strip() if 내용 else "못 찾음"
    기자 = soup.find("span", class_="byline_s")
    기자데이터 = 기자.text.strip() if 기자 else "못 찾음"
    # {} origin dic형태
    df1 = pd.DataFrame({
        "제목": [제목데이터],
        "내용": [내용데이터],
        "기자": [기자데이터],
    })
    # 근래에는 dict() 형태로 많이 사용하는 트렌드 컬럼이름을 "" 나 '' 로 감싸지 않는다.
    df2 = pd.DataFrame(
        dict(
            제목=[제목데이터],
            내용=[내용데이터],
            기자=[기자데이터],
        )
    )
    df2.to_csv("requests이용한naver뉴스수집.csv", index=False, encoding="utf-8-sig")
    print("requests이용한naver뉴스수집.csv 파일 저장 완료")


def 방법2번():
    아티클 = newspaper.article(url, language="ko")
    아티클.parse()

    제목 = 아티클.title
    내용 = 아티클.text
    기자 = 아티클.authors
    날짜 = 아티클.publish_date

    df = pd.DataFrame({
        "제목": [제목],
        "내용": [내용],
        "기자": [기자],
    })

    df.to_csv("requests이용한naver뉴스수집.csv", index=False, encoding="utf-8-sig")
    print("newspaper이용한naver뉴스수집.csv 파일 저장 완료")


방법1번()
방법2번()
