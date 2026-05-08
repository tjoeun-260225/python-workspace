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
    df.to_csv("맛집크롤링결과.csv", index=False, encoding='utf-8-sig')
    print("맛집크롤링결과.csv 저장 완료")
    return df


# ===========================
# 3단계 : WordCloud
# ===========================
def 워드클라우드생성(df):
    all_text = ' '.join(df["본문"])
    okt = Okt()

    # TODO : all_text 에서 명사 추출 후 nouns 에 저장
    nouns = okt.nouns(all_text)

    # TODO : 기존 불용어 + 네이버 UI 노이즈 불용어 추가
    # 기존 : {'것', '수', '등', '곳', '더', '이', '맛집', '네이버'}
    # 추가할 것 : 'NAVER', '검색', '영역', '바로가기', '로그인', '서비스',
    #             '본문', '메뉴', '다음', '이전', '안내', '결과', '지도',
    #             '업체', '광고', '영업', '예약', '주문', '포장', '쿠폰',
    #             '필터', '전체', '등록', '확대', '축소', '이미지', '뉴스',
    #             '블로그', '카페', '쇼핑', '동영상', '지식', '도서',
    #             '플레이스', '플러스', '레이어', '사용자', '링크', '입력기'
    stopwords = {'것', '수', '등', '곳', '더', '이', '맛집', '네이버',
                 'NAVER', '검색', '영역', '바로가기', '로그인', '서비스',
                 '본문', '메뉴', '다음', '이전', '안내', '결과', '지도',
                 '업체', '광고', '영업', '예약', '주문', '포장', '쿠폰',
                 '필터', '전체', '등록', '확대', '축소', '이미지', '뉴스',
                 '블로그', '카페', '쇼핑', '동영상', '지식', '도서',
                 '플레이스', '플러스', '레이어', '사용자', '링크', '입력기'}

    filtered = [w for w in nouns if w not in stopwords and len(w) >=2 ]

    # TODO : Counter 로 단어 빈도 계산 후 counts 에 저장
    counts = Counter(filtered)

    # TODO : 상위 10개 키워드 출력
    print(counts.most_common(10))

    # TODO : 한글 폰트 경로 설정
    font_path = 'C:/Windows/Fonts/malgun.ttf'

    # TODO : WordCloud 생성 (font_path, width=800, height=400, background_color='white', colormap='Set2')
    wc = WordCloud(font_path=font_path,
                   width=800,
                   height=400,
                   background_color='white',
                   colormap='Set2').generate_from_frequencies(counts)

    plt.figure(figsize=(12, 6))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('맛집_wordcloud.png' , dpi=150)
    plt.show()


# ===========================
# 💡💡💡💡💡 실행 💡💡💡💡💡
# ===========================
결과 = 맛집리뷰수집()
df = csv저장(결과)
워드클라우드생성(df)
