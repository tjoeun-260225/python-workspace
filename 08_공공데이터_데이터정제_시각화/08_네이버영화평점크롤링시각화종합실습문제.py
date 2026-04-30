from playwright.sync_api import sync_playwright
import pandas as pd
import matplotlib.pyplot as plt
import re
import time

# =============================================
# PART 1. 크롤링 & CSV 저장
# =============================================

영화목록 = ["왕과 사는 남자", "범죄도시4", "파묘", "서울의봄", "탑건매버릭",
        "아바타2", "한산", "범죄도시2", "모가디슈", "엘리멘탈"]
결과리스트 = []

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
page = browser.new_page()

for 영화 in 영화목록:
    page.goto(f"https://search.naver.com/search.naver?query={영화}+영화")
    time.sleep(2)

    제목 = page.title()
    본문 = page.locator("body").inner_text()

    # 실관람객 평점 파싱
    실관람객 = re.search(r"[★*]?\s*(\d+\.\d+)", 본문)
    실관람객평점 = float(실관람객.group(1)) if 실관람객 else None
    # 네티즌 평점 파싱
    네티즌 = re.search(r"네티즌\s*평점?\s*(\d+\.\d+)", 본문)
    네티즌평점 = 실관람객평점

    # 관객수 파싱 (예: "1,673만" or "1673만")
    관객 = re.search(r"관객수\s*([\d,]+)만명?", 본문)
    관객수 = int(관객.group(1).replace(",", "")) if 관객 else None
    # 장르 파싱
    장르 = re.search(r"개요\s*([가-힣A-Za-z]+)[·\s]", 본문)
    장르명 = 장르.group(1) if 장르 else None

    print(f"=== {영화}")
    print(f"실관람객평점: {실관람객평점}, 네티즌평점: {네티즌평점}, 관객수: {관객수}, 장르: {장르명}")

    결과리스트.append([영화, 실관람객평점, 네티즌평점, 관객수, 장르명])

    time.sleep(2)

browser.close()
p.stop()

df = pd.DataFrame(결과리스트, columns=["영화명", "실관람객평점", "네티즌평점", "관객수", "장르"])
df.to_csv("영화평점.csv", index=False, encoding="utf-8-sig")
print("저장 완료")


# =============================================
# PART 2. 시각화
# =============================================

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

df = pd.read_csv("영화평점.csv", encoding="utf-8-sig")

# 문제 6. 막대 그래프
plt.bar(df["영화명"], df["실관람객평점"])
plt.title("영화별 실관람객 평점")
plt.xlabel("영화명")
plt.ylabel("실관람객평점")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 문제 7. 파이 차트
장르별_수 = df["장르"].value_counts()
plt.pie(
    장르별_수.values,
    labels=장르별_수.index,
    autopct="%.1f%%"
)
plt.title("장르별 영화 비율")
plt.show()

# 문제 8. 히스토그램
plt.hist(df["관객수"], bins=5)
plt.title("영화 관객수 분포")
plt.xlabel("관객수 (만명)")
plt.ylabel("영화 수")
plt.show()

# 문제 9. 산점도
plt.scatter(df["실관람객평점"], df["네티즌평점"], alpha=0.7)
plt.title("실관람객평점 vs 네티즌평점")
plt.xlabel("실관람객평점")
plt.ylabel("네티즌평점")
plt.show()

# 문제 10. 이미지 저장
plt.bar(df["영화명"], df["실관람객평점"])
plt.title("영화별 실관람객 평점")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("영화평점_차트.png")
plt.show()