import requests
import newspaper
from bs4 import BeautifulSoup
import time

# 브라우저인 척 하는 헤더
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
}


# ① 네이트 종합 랭킹 페이지에서 URL 20개 가져오기
def url목록가져오기():
    # 네이트 종합 랭킹 뉴스 주소
    랭킹주소 = "https://news.nate.com/rank/interest?sc=its"

    # TODO: requests.get() 으로 랭킹 페이지에 요청 보내기
    res = requests.get(랭킹주소, headers=headers)

    # TODO: BeautifulSoup 으로 HTML 파싱하기
    soup = BeautifulSoup(res.text, "html.parser")

    # 힌트: F12 개발자도구로 기사 링크 태그 확인 후 작성
    # 힌트: soup.select("a.태그명") 형식으로 작성
    # TODO: 기사 링크 태그 전부 찾기
    태그들 = soup.select("a.lt1")

    랭크목록 = []
    for 태그 in 태그들[:20]:  # 최대 20개

        # TODO: 태그에서 href 속성(링크주소) 꺼내기
        링크 = 태그.get("href")

        if 링크:
            # 상대경로면 절대경로로 변환
            if 링크.startswith("/"):
                링크 = "https://news.nate.com" + 링크
            랭크목록.append(링크)

    print(f"총 {len(랭크목록)}개 URL 수집 완료!")
    return 랭크목록


# ② 기사 URL 1개로 제목 / 내용 / 기자 / 날짜 수집
def 기사수집(url):
    # TODO: newspaper4k 로 기사 객체 만들기 (language="ko")
    아티클 = newspaper.article(url, language="ko")

    아티클.parse()

    # TODO: requests.get() 으로 해당 url 에 요청 보내기
    res = requests.get(url, headers=headers)

    # TODO: BeautifulSoup 으로 HTML 파싱하기
    soup = BeautifulSoup(res.text, "html.parser")
    언론사태그 = soup.find("a", class_="medium")
    # <span class="sub_tit">이재명 대통령, 국무회의 발언<br>(서울=연합뉴스) 김도훈 기자 = 이재명 대통령이 28일 청와대에서 열린 국무회의 겸 비상경제점검회의에서 발언하고 있다. 2026.4.28 superdoo82@yna.co.kr</span></span>

    # TODO: 날짜 태그 찾기
    날짜태그 = soup.find("span", class_="firstDate")

    # TODO: 각 변수에 텍스트 값 저장 (없으면 "못 찾음" 출력)
    제목 = 아티클.title or "못 찾음"
    내용 = 아티클.text[:100] + "..." or "못 찾음"
    기자 = 언론사태그.text.strip() if 언론사태그 else "못 찾음"
    날짜 = 날짜태그.find("em").text.strip() if 날짜태그 else "못 찾음"

    return 제목, 내용, 기자, 날짜


# ③ 전체 실행
def 뉴스20개수집():
    # TODO: url목록가져오기() 함수 호출해서 url목록 변수에 저장
    url목록 = url목록가져오기()

    for i, url in enumerate(url목록):
        print(f"\n[ {i + 1}번째 기사 ]")

        # TODO: 기사수집() 함수 호출해서 변수에 저장
        제목, 내용, 기자, 날짜 = 기사수집(url)

        # TODO: 결과 출력
        print("제목 :", 제목)
        print("기자 :", 기자)
        print("날짜 :", 날짜)
        print("내용 :", 내용)

        time.sleep(2)  # TODO: 서버 차단 방지 (건드리지 말것)

    print("\n수집 완료")


# 실행
뉴스20개수집()
