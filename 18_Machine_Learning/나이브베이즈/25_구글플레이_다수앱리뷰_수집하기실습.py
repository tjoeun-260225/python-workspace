import pandas as pd
from google_play_scraper import reviews, Sort

앱목록 = {
    "카카오톡": "com.kakao.talk",
    "배달의민족": "com.us.mobile.korilla",
    "쿠팡": "com.coupang.mobile",
    "토스": "viva.republica.toss",
}


# ================================
# STEP 1. 앱 리뷰 수집하기
# ================================
def 앱리뷰수집(앱이름, 앱ID, 개수=1000):
    result, _ = reviews(앱ID, lang='ko', country="kr", sort=Sort.NEWEST, count=개수)

    리뷰목록 = []

    for item in result:
        리뷰목록.append({
            'app': 앱이름,  # 앱이름 그대로
            'review': item.get('content'),  # 리뷰 내용 키 이름은 'content'
            'rating': item.get('score'),  # 평점 키 이름은 'score'
        })

    print(f"수집완료: {앱이름} ({len(리뷰목록)}개)")
    return 리뷰목록


# ================================
# STEP 2. 전체 앱 수집 후 CSV 저장
# ================================
def csv_저장하기():
    전체데이터 = []

    for 이름, ID in 앱목록.items():
        리뷰 = 앱리뷰수집(이름, ID)
        전체데이터.extend(리뷰)  # 리스트 합치는 메서드

    df = pd.DataFrame(전체데이터)
    df.to_csv('csvs/google_app_review.csv', index=False, encoding='utf-8-sig')
    print(f"\n총 {len(df)}개 저장완료")
    print(df['app'].value_counts())
    return df

csv_저장하기()
