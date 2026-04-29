from playwright.sync_api import sync_playwright
import time
import csv  # pandas 를 사용하면 쓸 일 이 없다.
import pandas as pd


def 기본csv버전():  # pandas를 이용하지 않는 구버전
    p = sync_playwright().start()
    웹사이트 = p.chromium.launch(headless=False)
    page = 웹사이트.new_page()
    검색어목록 = ["강아지", "고양이", "토끼"]

    # 검색된 결과를 담을 목록 세팅
    검색결과리스트 = []
    for 검색어 in 검색어목록:
        page.goto(f"https://search.naver.com/search.naver?query={검색어}")
        제목 = page.title()
        검색결과리스트.append([검색어, 제목])
        time.sleep(2)

    # pandas 도구를 이용하지 않은 구버전방식
    f = open('네이버검색결과.csv', "w", newline="", encoding="utf-8-sig")  # 작성할 파일 생성하며 열기 작성모드 한글깨짐 방지
    wrter = csv.writer(f)
    wrter.writerow(["검색어", "페이지제목"])  # 컬럼 이름
    wrter.writerows(검색결과리스트)  # 각 컬럼에 해당하는 데이터들
    f.close()
    웹사이트.close()
    p.stop()


def pandasCsv버전():  # pandas를 이용하지 않는 구버전
    p = sync_playwright().start()
    웹사이트 = p.chromium.launch(headless=False)
    page = 웹사이트.new_page()
    검색어목록 = ["강아지", "고양이", "토끼"]

    # 검색된 결과를 담을 목록 세팅
    검색결과리스트 = []
    for 검색어 in 검색어목록:
        page.goto(f"https://search.naver.com/search.naver?query={검색어}")
        제목 = page.title()
        검색결과리스트.append([검색어, 제목])
        time.sleep(2)

    df = pd.DataFrame(검색결과리스트, columns=["검색어", "페이지제목"])
    df.to_csv('네이버검색결과.csv', index=False, encoding="utf-8-sig")
    웹사이트.close()
    p.stop()
pandasCsv버전()