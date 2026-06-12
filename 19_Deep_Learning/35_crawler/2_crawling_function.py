import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 힌트: def 함수이름(매개변수1, 매개변수2): 형태로 작성
# 검색어와 폴더이름을 매개변수로 받는 함수를 만들어라
def 이미지수집(키워드, 폴더이름):          # (1) 함수명, 매개변수 2개

    SAVE_DIR = 폴더이름                    # (2) 폴더이름 매개변수 사용
    os.makedirs(SAVE_DIR, exist_ok=True)

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # 힌트: 고정된 "강아지" 대신 매개변수를 f-string에 넣어라
        url = f"https://search.naver.com/search.naver?ssc=tab.image.all&where=image&sm=tab_jum&query={키워드}"
        # (3) 검색어 매개변수를 url에 삽입
        driver.get(url)
        time.sleep(3)

        for _ in range(10):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        images = driver.find_elements(By.TAG_NAME, "img")
        image_urls = set()

        for img in images:
            src = (
                    img.get_attribute("src")
                    or img.get_attribute("data-src")
                    or img.get_attribute("data-lazy-src")
            )
            if src and src.startswith("http"):
                image_urls.add(src)

        print(f"수집된 이미지 URL 수: {len(image_urls)}")

        count = 1
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

        for img_url in image_urls:
            try:
                response = requests.get(img_url, headers=headers, timeout=10)
                if response.status_code == 200:
                    # 힌트: 고정된 "dog" 대신 매개변수를 파일명에 넣어라
                    filename = os.path.join(SAVE_DIR, f"{폴더이름}{count}.jpg")
                    # (4) 영어폴더이름 매개변수를 파일명에 삽입
                    with open(filename, "wb") as f:
                        f.write(response.content)
                    print(f"저장 완료: {filename}")
                    count += 1
            except Exception as e:
                print("다운로드 실패:", e)

    finally:
        driver.quit()

    # 힌트: 어떤 동물 수집이 끝났는지 출력
    print(f"{키워드} 완료")   # (5) 검색어 매개변수 출력


# 힌트: 만든 함수를 3번 호출해서 토끼, 사자, 호랑이를 수집해라
이미지수집("토끼",   "rabbit")   # (6)
이미지수집("사자",   "lion")   # (7)
이미지수집("호랑이", "tiger")   # (8)