import requests
import newspaper
from bs4 import BeautifulSoup
import time

# 봇 차단 우회
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://news.nate.com/",
    "Connection": "keep-alive",
}

# 세션 사용 (쿠키 유지 → 차단 줄어듦)
session = requests.Session()
session.headers.update(headers)


def url목록가져오기():
    랭킹주소 = "https://news.nate.com/rank/interest?sc=its"

    try:
        res = session.get(랭킹주소, timeout=10)
        res.raise_for_status()
    except Exception as e:
        print(f"랭킹 페이지 요청 실패: {e}")
        return []

    soup = BeautifulSoup(res.text, "html.parser")
    태그들 = soup.select("a.lt1")

    랭크목록 = []
    for 태그 in 태그들[:20]:
        링크 = 태그.get("href")
        if not 링크:
            continue

        # // 로 시작하는 경우 (프로토콜 없는 절대경로)
        if 링크.startswith("//"):
            링크 = "https:" + 링크
        # / 로 시작하는 경우 (상대경로)
        elif 링크.startswith("/"):
            링크 = "https://news.nate.com" + 링크

        랭크목록.append(링크)

    print(f"총 {len(랭크목록)}개 URL 수집 완료!")
    return 랭크목록


def 기사수집(url):
    try:
        res = session.get(url, timeout=10)
        res.raise_for_status()
    except Exception as e:
        print(f"  기사 요청 실패: {e}")
        return "못 찾음", "못 찾음", "못 찾음", "못 찾음"

    soup = BeautifulSoup(res.text, "html.parser")

    # 제목
    제목태그 = soup.find("h1", class_="articleSubecjt")
    제목 = 제목태그.text.strip() if 제목태그 else "못 찾음"

    # 본문 (realArtcContents 안의 텍스트)
    본문태그 = soup.find("div", id="realArtcContents")
    if 본문태그:
        내용 = 본문태그.get_text(separator=" ", strip=True)[:150] + "..."
    else:
        내용 = "못 찾음"

    # 언론사
    언론사태그 = soup.find("a", class_="medium")
    기자 = 언론사태그.text.strip() if 언론사태그 else "못 찾음"

    # 날짜
    날짜태그 = soup.find("span", class_="firstDate")
    if 날짜태그:
        em = 날짜태그.find("em")
        날짜 = em.text.strip() if em else "못 찾음"
    else:
        날짜 = "못 찾음"

    return 제목, 내용, 기자, 날짜


def 뉴스20개수집():
    url목록 = url목록가져오기()

    if not url목록:
        print("URL 수집 실패. 종료합니다.")
        return

    for i, url in enumerate(url목록):
        print(f"\n[ {i + 1}번째 기사 ]")
        print(f"URL: {url}")

        제목, 내용, 기자, 날짜 = 기사수집(url)

        print("제목 :", 제목)
        print("기자(언론사) :", 기자)
        print("날짜 :", 날짜)
        print("내용 :", 내용)

        time.sleep(2)  # 서버 차단 방지

    print("\n수집 완료")


뉴스20개수집()