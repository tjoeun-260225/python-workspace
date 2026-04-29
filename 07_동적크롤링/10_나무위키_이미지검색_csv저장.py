import pandas as pd
from playwright.sync_api import sync_playwright
import requests
import os
import time


def 단일_이미지_csv_저장():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    os.makedirs("나무위키이미지", exist_ok=True)
    검색어 = "너구리"
    page.goto(f"https://namu.wiki/w/{검색어}")

    제목 = page.title()
    본문 = page.locator("body").inner_text()

    time.sleep(2)

    이미지데이터 = page.locator(".D3JLvbdh").all()
    print("이미지데이터들 : ", 이미지데이터)
    이미지주소 = None
    for 이미지 in 이미지데이터:
        alt = 이미지.get_attribute("alt") or ""
        주소 = 이미지.get_attribute("src")

        if 주소 and "아이콘" not in alt:
            이미지주소 = 주소
            break
    if 이미지주소.startswith("//"):
        이미지주소 = "https:" + 이미지주소
        확장자 = 이미지주소.split(".")[-1].split("?")[0]
        if 확장자 not in ["jpg", "jpeg", "png", "webp", "gif"]:
            확장자 = "jpg"
        try:
            응답 = requests.get(이미지주소, timeout=5)
            파일이름 = f"나무위키이미지/{검색어}.{확장자}"
            f = open(파일이름, "wb")
            f.write(응답.content)
            f.close()
            print(f"저장완료 : {파일이름}")
        except:
            print("이미지 저장 실패")
    else:
        print("이미지 URL 없음")

    browser.close()
    p.stop()

    # CSV 저장
    # 결과 데이터 가져와서 정렬
    결과데이터 = [[검색어, 제목, 본문[:300], 이미지주소, 파일이름]]
    df = pd.DataFrame(결과데이터, columns=["검색어","제목","본문(앞300자)","이미지URL","이미지파일경로"])
    df.to_csv("너구리_나무위키.csv", index=False, encoding="utf-8-sig")

    print("완료")

단일_이미지_csv_저장()

from playwright.sync_api import sync_playwright
import requests
import os
import time

def 다수이미지():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    os.makedirs("나무위키이미지", exist_ok=True)
    키워드목록 =["너구리","고양이","강아지","판다","호랑이"]

    for 키워드 in 키워드목록:
        page.goto(f"https://namu.wiki/w/{키워드}")
        time.sleep(2)
        이미지데이터 = page.locator("img").all()

        이미지주소 = None
        for 이미지 in 이미지데이터:

            alt = 이미지.get_attribute("alt") or ""
            주소 = 이미지.get_attribute("src")

            if 주소 and "아이콘" not in alt:
                이미지주소 = 주소
                break
        if 이미지주소:
            if 이미지주소.startswith("//"):
                이미지주소 = "https:" + 이미지주소
            확장자 = 이미지주소.split(".")[-1].split("?")[0]
            if 확장자 not in ["jpg","png","jpeg","webp","gif"]:
                확장자 = "jpg"

            try:
                응답 = requests.get(이미지주소, timeout=5)
                파일이름 = f"나무위키이미지/{키워드}.{확장자}"

                f = open(파일이름, "wb")
                f.write(응답.content)
                f.close()
                print(f"저장완료 : {파일이름}")
            except:
                print(f"{키워드} 다운로드 실패")
        else:
            print(f"{키워드} 이미지 없음")
        time.sleep(2)
    browser.close()
    p.stop()
    print("전체 저장 완료")

다수이미지()