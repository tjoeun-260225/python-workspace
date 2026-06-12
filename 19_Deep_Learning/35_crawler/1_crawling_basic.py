import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# ───────────────────────────────────────────────
# 지금은 강아지 하나만 수집할 수 있다.
# 토끼, 사자, 호랑이도 수집하려면 이 코드를 3번 복사해야 한다.
# → def 함수로 만들어서 해결해보자
# ───────────────────────────────────────────────

SAVE_DIR = "dog"
os.makedirs(SAVE_DIR, exist_ok=True)

크롬옵션 = Options()
크롬옵션.add_argument("--start-maximized")
드라이버 = webdriver.Chrome(options=크롬옵션)

try:
    url = "https://search.naver.com/search.naver?ssc=tab.image.all&where=image&sm=tab_jum&query=강아지"
    드라이버.get(url)
    time.sleep(3)

    for _ in range(10):
        드라이버.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    이미지들 = 드라이버.find_elements(By.TAG_NAME, "img")
    이미지_주소들 = set()

    for 이미지 in 이미지들:
        src속성 = (
                이미지.get_attribute("src")
                or 이미지.get_attribute("data-src")
                or 이미지.get_attribute("data-lazy-src")
        )
        if src속성 and src속성.startswith("http"):
            이미지_주소들.add(src속성)

    print(f"수집된 이미지 URL 수: {len(이미지_주소들)}")

    count = 1
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    for 이미지_주소 in 이미지_주소들:
        try:
            응답 = requests.get(이미지_주소, headers=headers, timeout=10)
            if 응답.status_code == 200:
                파일이름 = os.path.join(SAVE_DIR, f"dog_{count}.jpg")
                with open(파일이름, "wb") as f:
                    f.write(응답.content)
                print(f"저장완료: {파일이름}")
                count += 1
        except Exception as e:
            print("다운로드 실패:", e)

finally:
    드라이버.quit()