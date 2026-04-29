# 스켈레톤 코드 = 뼈대 코드
from playwright.sync_api import sync_playwright
import time
import csv
import pandas as pd

'''
playwright 시작
    → 브라우저 열기
        → 검색어마다 페이지 이동
            → 제목 + 본문 가져오기
                → 결과 리스트에 추가
    → 브라우저 닫기
→ playwright 종료
→ CSV 파일로 저장
'''
'''
p = sync_playwright().start()                   sync_playwright().start()
browser = p.chromium.launch(headless=False)     sync_playwright().start().chromium.launch(headless=False)
page = browser.new_page()                       sync_playwright().start().chromium.launch(headless=False).new_page()

page.goto(f"https://namu.wiki/w/{검색}")        sync_playwright().start().chromium.launch(headless=False).new_page().goto(f"https://namu.wiki/w/{검색}")

locator("body").inner_text()

open("나무위키결과.csv", "w", newline="", encoding="utf-8-sig")


'''

def 나무위키_기본CSV버전():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    검색어목록 = ["강아지", "고양이", "토끼"]
    결과리스트 = []
    for 검색 in 검색어목록:
        page.goto(f"https://namu.wiki/w/{검색}")
        time.sleep(2)
        제목 = page.title()
        본문 = page.locator("body").inner_text()
        결과리스트.append([검색, 제목, 본문[:300]])
        time.sleep(2)
    browser.close()
    p.stop()
    f = open("나무위키결과.csv", "w", newline="", encoding="utf-8-sig")
    writer = csv.writer(f)
    writer.writerow(["검색어","제목","본문"])
    writer.writerows(결과리스트)
    f.close()
    print("기본CSV 저장 완료!")

# ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
def 나무위키_pandasCSV버전():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    검색어목록 = ["강아지", "고양이", "토끼"]
    결과리스트 = []
    for 검색 in 검색어목록:
        page.goto(f"https://namu.wiki/w/{검색}")
        time.sleep(2)
        제목 = page.title()
        본문 = page.locator("body").inner_text()
        결과리스트.append([검색, 제목, 본문[:300]])
        time.sleep(2)
    browser.close()   # 열려 있는 상태에서 데이터 csv로 저장하면 메모리 소요 크기 때문에 닫기
    p.stop()
    df = pd.DataFrame(결과리스트, columns=["검색어","제목","본문"])
    df.to_csv("나무위키결과.csv", index=False, encoding="utf-8-sig")
    print("pandas CSV 저장 완료!")


# 나무위키_기본CSV버전()
나무위키_pandasCSV버전()