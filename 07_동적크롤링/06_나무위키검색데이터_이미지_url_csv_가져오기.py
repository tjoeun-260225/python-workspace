from playwright.sync_api import sync_playwright
import pandas as pd
import time

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
page = browser.new_page()

검색어목록 = ["강아지","고양이","토끼"]
결과리스트 = []

for 검색 in 검색어목록:
    page.goto(f"https://namu.wiki/w/{검색}")
    time.sleep(2)

    제목 = page.title()

    # 이미지 태그 찾아서 src 속성 (이미지 URL)갖고오기
    # <img src="이미지경로">
    이미지목록 = page.locator("img").all() # 이미지 모두~가져오기
    이미지URL = ""
    if 이미지목록: # 이미지가 하나라도 있으면 True   1 = True  0 = False
        이미지URL = 이미지목록[0].get_attribute("src") # 두 번째 나 세번째 이미지는 존재하는지 모르기 때문에 우선 맨 첫번재이미지 경로만 갖고오기

    print(f"==={검색}")
    print(f"제목 : {제목}")
    print(f"이미지URL : {이미지URL}")
    print()

    # TODO : 결과리스트에 검색 제목 이미지URL 추가
    # TODO : 2초간 정지

# TODO : browser 맨 나중에 연 것부터 맨 처음 연것을 닫기
# 파티를 연 사람이 맨 나중에 정리하고 퇴장하는 것처럼 나중에 연것을 순차적으로 닫기 처리해서 문제가 생기지 않도록 한다.

# TODO : pandas DataFrame 에 결과리스트를 컬럼명칭 = 검색어 제목 이미지경로 로 지정해서 틀 세팅
# TODO : 세팅된 틀과 데이터를 to_CSV 이용해서 저장 나무위키_이미지데이터.csv 순번없이 한글깨짐 방지













