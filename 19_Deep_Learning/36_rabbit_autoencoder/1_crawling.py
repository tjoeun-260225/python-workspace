import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def 이미지저장(검색어, 영어폴더이름):
    SAVE_DIR = 영어폴더이름
    os.makedirs(SAVE_DIR, exist_ok=True)

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        url = f"https://search.naver.com/search.naver?ssc=tab.image.all&where=image&sm=tab_jum&query={검색어}"
        driver.get(url)
        time.sleep(3)

        # 스크롤을 10번 내려서 더 많은 이미지 로드
        for _ in range(10):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        # img 태그에서 URL 수집
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

        # 이미지 다운로드
        count = 1
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        for img_url in image_urls:
            try:
                response = requests.get(img_url, headers=headers, timeout=10)
                if response.status_code == 200:
                    filename = os.path.join(SAVE_DIR, f"{영어폴더이름}_{count}.jpg")
                    with open(filename, "wb") as f:
                        f.write(response.content)
                    print(f"저장 완료: {filename}")
                    count += 1
            except Exception as e:
                print("다운로드 실패:", e)
    finally:
        driver.quit()
    print(f"{검색어} 완료")

이미지저장("토끼", "rabbit")