# 뉴스를 보고 분석
import requests
import newspaper
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
}

url = "https://n.news.naver.com/article/277/0005755604?ntype=RANKING"

# 네이버 뉴스 랭킹 페이지에서 URL 20개 자동 수집
def url목록가져오기():
    랭킹주소 = "https://news.naver.com/main/ranking/popularDay.naver"
    res = requests.get(랭킹주소,headers=headers)
    soup = BeautifulSoup(res.text,"html.parser")

    랭크목록 = []
    태그들 = soup.select("a.list_title")

    for 태그 in 태그들[:20]: #최대 20개 까지만 설정 0~19 까지
        링크 = 태그.get("href")
        if 링크 and "article" in 링크 :
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
    내용 = 아티클.text[:100] + "..." # 내용이 너무 길면 100자까지만 가져오고 나머지 ... 보여주기 처리
    기자 = 기자태그.text.strip() if 기자태그 else "못 찾음"
    날짜 = 날짜태그.text.strip() if 날짜태그 else "못 찾음"

    return 제목, 내용, 기자, 날짜















