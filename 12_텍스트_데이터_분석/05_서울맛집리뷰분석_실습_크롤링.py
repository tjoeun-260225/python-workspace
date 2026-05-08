from playwright.sync_api import sync_playwright
from konlpy.tag import Okt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import time


# ===========================
# 1단계 : 크롤링
# ===========================

def 맛집리뷰수집():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    키워드목록 = ["강남 맛집", "홍대 맛집", "명동 맛집"]

    결과리스트 = []

    for 키워드 in 키워드목록:
        page.goto(f"https://search.naver.com/search.naver?query={키워드}")
        time.sleep(2)
        제목 = page.title()
        본문 = page.locator('body').inner_text()
        결과리스트.append([키워드, 제목, 본문[:500]])

        time.sleep(2)
    browser.close()
    p.stop()

    return 결과리스트


# ===========================
# 2단계 : CSV 저장
# ===========================

def csv저장(결과리스트):
    df = pd.DataFrame(결과리스트, columns=["키워드", "제목", "본문"])
    df.to_csv('맛집크롤링결과.csv', index=False, encoding='utf-8-sig')
    print("맛집크롤링결과.csv 저장 완료")
    return df


# ===========================
# 3단계 : WordCloud
# ===========================

def 워드클라우드생성(df):
    all_text = ' '.join(df['본문'])
    okt = Okt()
    nouns = okt.nouns(all_text) # 은 는 이 가 에게 와 같이 누가봐도 필요하지 않을 것같은 단어 필터
    # stopwords = nouns 를 만든 개발자가 생각치 못했거나, 우리 회사 입장에서 불필요한 단어를 모두 작성
    stopwords = {'것', '수', '등', '곳', '더', '이', '맛집', '네이버', '지도', '검색', '보기', '메뉴', '영역', '바로가기', '카페', '지식'}
    filtered = [w for w in nouns if w not in stopwords and len(w) >= 2]
    counts = Counter(filtered)
    print(counts.most_common(10))
    font_path = 'C:/Windows/Fonts/malgun.ttf'
    wc = WordCloud(font_path=font_path,
                   width=800,
                   height=400,
                   background_color='white',
                   colormap='Set2').generate_from_frequencies(counts)

    plt.figure(figsize=(12, 6))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('맛집_wordcloud.png', dpi=150)
    plt.show()


# ===========================
# 💡💡💡💡💡 실행 💡💡💡💡💡
# ===========================

결과 = 맛집리뷰수집()
df = csv저장(결과)
워드클라우드생성(df)
