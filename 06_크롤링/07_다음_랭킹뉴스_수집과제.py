import requests
import newspaper
from bs4 import BeautifulSoup
import time

# 브라우저인 척 하는 헤더 (없으면 차단당할 수 있음)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
}


# ① 다음 랭킹 뉴스 페이지에서 URL 20개 가져오기
def url목록가져오기():
    랭킹주소 = "https://entertain.daum.net/ranking/popular"

    res = requests.get(랭킹주소, headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    태그들 = soup.select("a.link_thumb")

    랭크목록 = []
    for 태그 in 태그들[:20]:  # 최대 20개

        링크 = 태그.get("href")
        # 상대 경로일 때 체크를 제외하고 링크 수집 진행
        if 링크 and "article" in 링크:
            if 링크.startswith("/"):
                링크 = "https://news.daum.net" + 링크
            if 링크 not in 랭크목록:
                랭크목록.append(링크)
        if len(랭크목록) >= 20:
            break

    print(f"총 {len(랭크목록)}개 URL 수집 완료!")
    return 랭크목록


# ② 기사 URL 1개로 제목 / 내용 / 기자 / 날짜 수집
def 기사수집(url):
    # TODO: newspaper4k 로 기사 객체 만들기 (language="ko")
    아티클 = newspaper.article(url, headers=headers)

    # TODO: 기사 파싱하기
    아티클.parse()

    # TODO: requests.get() 으로 해당 url 에 요청 보내기
    # 주소 하나하나 접속해서 요청 보내는 것
    res = requests.get(url, headers=headers)

    # TODO: BeautifulSoup 으로 HTML 파싱하기
    soup = BeautifulSoup(res.text, "html.parser")

    # 힌트: 크롬 개발자도구(F12) 로 기자 / 날짜 태그 확인 후 작성
    # TODO: 기자 태그 찾기
    기자태그 = soup.find("span", class_="txt_info")

    # TODO: 날짜 태그 찾기
    날짜태그 = soup.find("span", class_="num_date")

    # TODO: 각 변수에 텍스트 값 저장하기 (없으면 "못 찾음" 출력)
    제목 = 아티클.title
    내용 = 아티클.text[:100] + "..."  # 내용은 100자만
    기자 = 기자태그.text.strip() if 기자태그 else "못 찾음"
    날짜 = 날짜태그.text.strip() if 날짜태그 else "못 찾음"

    return 제목, 내용, 기자, 날짜


# ③ 전체 실행 함수
def 뉴스20개수집():
    # TODO: url목록가져오기() 함수 호출해서 url목록 변수에 저장
    url목록 = url목록가져오기()

    for i, url in enumerate(url목록):
        print(f"\n[ {i + 1}번째 기사 ]")

        # TODO: 기사수집() 함수 호출해서 제목,내용,기자,날짜 변수에 저장
        제목, 내용, 기자, 날짜 = 기사수집(url)

        # TODO: 제목 / 기자 / 날짜 / 내용 출력하기
        print("제목 :", 제목)
        print("기자 :", 기자)
        print("날짜 :", 날짜)
        print("내용 :", 내용)
        time.sleep(2)

    print("\n수집 완료")


# 실행
뉴스20개수집()
