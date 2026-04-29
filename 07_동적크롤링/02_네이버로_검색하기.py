from playwright.sync_api import sync_playwright
import time

p = sync_playwright().start()  # 크롤링을 시작하겠다!
웹사이트 = p.chromium.launch(headless=False)  # 크롬을 이용해서 검색 시작하겠다. head 는 없다
page = 웹사이트.new_page()  # 웹사이트 새 페이지 띄우기 기능
# 검색어 리스트로 강아지 고양이 토끼 넣고 for 문을 이용해서 강아지 검색하고 고양이 검색하고 토끼 검색하기

검색어목록 = ["강아지", "고양이", "토끼"]

for 검색어 in 검색어목록:
    page.goto(f"https://search.naver.com/search.naver?query={검색어}")
    print(page.title())
    time.sleep(2)  # 2초 대기후 다음 검색
웹사이트.close()  # 웹사이트 창 닫기
p.stop()  # 크롤링 종료
