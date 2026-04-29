from playwright.sync_api import sync_playwright
import time
'''
playwright 시작
    → 브라우저 열기
            →  검색어마다 페이지 이동
                → 제목 + 본문 가져오기
                    →  출력
    →  브라우저 닫기
→  playwright 종료
'''

def 나무위키기본():
    p = sync_playwright().start()   # playwright 실행 시작
    browser = p.chromium.launch(headless=False) # 크롬 브라우저 열기 headless=False 검색하는 창 보이기 True 하면 검색하는 상황 안보임
    page = browser.new_page() # 새 탭(페이지)열기

    검색어목록 = ["강아지", "고양이", "토끼"] # 검색할 단어 리스트

    for 검색 in 검색어목록: #검색어 하나씩꺼내서 반복
        page.goto(f"https://namu.wiki/w/{검색}") # 나무위키 해당 단어 페이지로 이동
        time.sleep(2) # 페이지 로딩 기다리기 2초

        제목 = page.title() # 브라우저 탭 제목가져오기
        본문 = page.locator("body").inner_text() # body 태그 안의 전체 텍스트 가져오기

        print(f"=== {검색}") # 현재 검색어 출력
        print(f"제목 : {제목}") # 제목 출력
        print(f"본문 앞부분 : {본문[:300]}") # 본문 앞 300글자만 출력
        print() # 검색어 사이 구분용

        time.sleep(2) # 다음 검색 전 2초 대기 너무 빠르게 검색하면 봇인것을 인지하고 차단될 수 있다.

    browser.close() # 열린 크롬 브라우저 닫기
    p.stop() # playwright 종료

나무위키기본()