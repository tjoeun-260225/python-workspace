# 06 번 뉴스 데이터 다수 수집 기준
# 뉴스를 보고 분석
import time

import requests
import newspaper
from bs4 import BeautifulSoup
import pandas as pd  # 이 줄 하나 추가

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
}

url = "https://n.news.naver.com/article/277/0005755604?ntype=RANKING"


def url목록가져오기():
    랭킹주소 = "https://news.naver.com/main/ranking/popularDay.naver"
    res = requests.get(랭킹주소, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    랭크목록 = []
    태그들 = soup.select("a.list_title")
    for 태그 in 태그들[:20]:
        링크 = 태그.get("href")
        if 링크 and "article" in 링크:
            if 링크.startswith("/"):
                링크 = "https://news.naver.com" + 링크
            랭크목록.append(링크)
    print(f"총 {len(랭크목록)} 개 URL 수집 완료")
    return 랭크목록


def 기사수집(url):
    아티클 = newspaper.article(url, language="ko")
    아티클.parse()

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    기자태그 = soup.find("span", class_="byline_s")
    날짜태그 = soup.find("span", class_="media_end_head_info_datestamp_time")

    제목 = 아티클.title
    내용 = 아티클.text[:100] + "..."  # 내용이 너무 길면 100자까지만 가져오고 나머지 ... 보여주기 처리
    기자 = 기자태그.text.strip() if 기자태그 else "못 찾음"
    날짜 = 날짜태그.text.strip() if 날짜태그 else "못 찾음"

    return 제목, 내용, 기자, 날짜


def 뉴스20개수집():
    url목록 = url목록가져오기()

    수집결과 = []  # 2. 수집한 데이터 담을 리스트 준비

    for i, url in enumerate(url목록):
        print(f"\n[ {i + 1}번째 뉴스 기사 ]")
        제목, 내용, 기자, 날짜 = 기사수집(url)
        print("제목 :", 제목)
        print("내용 :", 내용)
        print("기자 :", 기자)
        print("날짜 :", 날짜)
        # 3. 중간에 수집한 데이터를 수집결과 리스트에 append 추가
        수집결과.append(dict(제목=제목, 기자=기자, 날짜=날짜, 내용=내용))
        time.sleep(1)
    # 4. 반복 끝나고 최종적으로 데이터를 한 번에 저장
    df = pd.DataFrame(수집결과)
    df.to_csv("naver뉴스수집.csv", index=False, encoding="utf-8-sig")
    print("수집 완료")


뉴스20개수집()
