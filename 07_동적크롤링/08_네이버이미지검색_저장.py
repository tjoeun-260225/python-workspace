from playwright.sync_api import sync_playwright
import requests # 이미지 다운로드 용
import os       # 이미지 폴더 만들기 용
import time     # 잠시 대기하며 다음 검색을 위한 모듈

# from tests.demo_without_stealth_test import browser, page
# 잘못된 상태 모듈~~~
# ModuleNotFoundError: No module named 'pkg_resources' 보고 싶다면
# page = browser.new_page() 안하면 된다.

def 단일검색():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 이미지 저장할 폴더 만들기
    os.makedirs("다운로드이미지", exist_ok=True) # 폴더가 있으면 스킵 없으면 자동 생성
    # GetMapping("search.naver")
    # public String searchPage(@RequestParam String where, @RequestParam String query = "고양이"){}
    page.goto(f"https://search.naver.com/search.naver?where=image&query=고양이")
    time.sleep(2)

    # 고양이 이미지 데이터 가져오기
    이미지목록 = page.locator("._fe_image_tab_content_thumbnail_image").all()
    print(f"=== 고양이 : {len(이미지목록)}개 발견")

단일검색()

