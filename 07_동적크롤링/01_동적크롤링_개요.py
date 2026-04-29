'''
Selenium vs Playwright

Selenium
- 2004년 출시
- 가장 오래된 웹 자동화 도구
- 거의 모든 언어 지원
- 커뮤니티와 레퍼런스가 압도적으로 많음
- pip install selenium
- pip install webdriver-manager

Playwright
- 2020년 발표된 Microsoft 가 만든 자동화 도구
- 비동기 처리가 기본
- 속도가 빠르고 현대적인 웹앱에 강하다.
- pip install playwright
---- playwright 기능을 쓸 수 있게 해준다.
- playwright install
---- chrome firebox webkit(크롬 파이어폭스 이외 거의 모든 브라우저) 자체를 모두 다운로드
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def 셀레니움기본코드():
    # 브라우저 열기
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # 페이지 이동
    driver.get("https://google.com")
    # 요소 찾기 태그 안에 있는 데이터 찾기
    search_box = driver.find_element(By.NAME, "q")
    #텍스트 입력
    search_box.send_keys("셀레니움 이란")
    search_box.submit()
    #결과 출력
    print(driver.title)
    # 브라우저 닫기 = quit()
    driver.quit()
# 셀레니움기본코드()

from playwright.sync_api import sync_playwright

def playwright기본코드():
    # playwright시작
    p = sync_playwright().start()
    # 브라우저 열기
    browser = p.chromium.launch(
        headless=False,
        args=["--disable-blink-features=AutomationControlled"]
    )
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    )
    # 새 페이지
    #page = browser.new_page()
    page = context.new_page()
    page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    # 페이지 이동
    page.goto("https://google.com")
    # 요소 찾고 입력
    page.fill('textarea[name="q"]', 'Playwright 란')
    page.keyboard.press("Enter")
    # 결과 기다리기
    page.wait_for_load_state("networkidle")
    print(page.title())
    # 종료
    browser.close()
    p.stop()
playwright기본코드()









