import pandas as pd
from google_play_scraper import reviews, Sort

앱목록 = {
    "카카오톡"   : "com.kakao.talk",
    "배달의민족" : "com.us.mobile.korilla",
    "쿠팡"       : "com.coupang.mobile",
    "토스"       : "viva.republica.toss",
}


# ================================
# STEP 1. 앱 리뷰 한 개 수집하기
# ================================
def 앱리뷰수집(앱이름, 앱ID, 개수=100):
    # TODO 1: 리뷰 수집
    result, _ = reviews(앱ID, lang=___, country=___, sort=Sort.___, count=___)

    리뷰목록 = []

    for item in result:
        # TODO 2: 딕셔너리로 담기
        리뷰목록.append({
            'app'    : ___,          # 앱이름 그대로
            'review' : item.get(___),  # 리뷰 내용 키 이름은 'content'
            'rating' : item.get(___),  # 평점 키 이름은 'score'
        })

    print(f"수집완료: {앱이름} ({len(리뷰목록)}개)")
    return 리뷰목록


# ================================
# STEP 2. 전체 앱 수집 후 CSV 저장
# ================================
def csv_저장하기():
    전체데이터 = []

    for 이름, ID in 앱목록.___():
        # TODO 3: 앱리뷰수집 호출 후 전체데이터에 합치기
        리뷰 = 앱리뷰수집(___, ___)
        전체데이터.___(리뷰)          # 리스트 합치는 메서드

    # TODO 4: DataFrame 만들기
    df = pd.___(전체데이터)

    # TODO 5: CSV 저장
    df.to_csv(___, index=___, encoding=___)

    print(f"\n총 {len(df)}개 저장완료!")

    # TODO 6: 앱별 리뷰 개수 출력
    print(df[___].___())

    return df


# ================================
# 실행
# ================================
# TODO 7: 함수 실행
___()