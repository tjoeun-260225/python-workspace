# pickle ~ accuracy_score 경우 머신러닝에서 거의 필수로 작성
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# 아래는 모델과 사용할 데이터를 선택한 것 부가적인 사항
from google_play_scraper import reviews, Sort
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# =========================
# 1. 앱 리뷰 수집
# =========================


앱목록 = {
    "카카오톡": "com.kakao.talk",
    "쿠팡": "com.coupang.mobile",
    "토스": "viva.republica.toss",
}

전체데이터 = []
"""
                                                앱목록 = {
    "카카오톡"   "com.kakao.talk"                    "카카오톡": "com.kakao.talk",
    "쿠팡"       "com.coupang.mobile"                "쿠팡": "com.coupang.mobile",
    "토스        "viva.republica.toss"               "토스": "viva.republica.toss",
                                                      }

for 이름      ,  ID                        in 앱목록.items():

"""
for 이름, ID in 앱목록.items():
    # result 만 필요한데 reviews 라는 기능이 2가지를 반환하여
    # 오른쪽은 사용하지 않고 자리만 맞추겠다 _ 사용
    """
    reviews(
    ID,                어플의   고유 ID com.naver.shopping
    lang='ko',         리  뷰    언  어 ko = 한국어 en = 영어
    country='kr',      국            가 kr=한국 us=미국  
    sort=Sort.NEWEST,  정  렬    방  식 NEWEST(=최신순)  RATING(=평점순) HELPFULNESS(=도움된 순)
    count=2000         수집할 리뷰 개수
    )
    
    result , _
    리뷰    next_token, 다음페이지 이동용
    목록    다음페이지를 사용할 일이 없기 때문에 _ 버리는 것
            어플 리뷰의 경우 스크롤을 내려서 쭉 보는 형태로 페이지를 넘기는 형태가 아님
    """
    result, _ = reviews(ID, lang='ko', country='kr', sort=Sort.NEWEST, count=2000)
    # print dir(result) python2 버전에서 사용했던 print 문법
    for item in result:
        전체데이터.append({
            #   우리가 사용할 속성이름 설정 : 실제 result에서 가져온 값
            #                         'app': 이름,
            'app': 이름,
            'review': item.get('content'),
            'rating': item.get('score'),
        })
    print(f"수집완료 : {이름}({len(result)})개")
df = pd.DataFrame(전체데이터)

# =========================
# 2. 전처리 - 라벨 만들기
# =========================

df = df[df['rating'] != 3]  # 중립 제거
df = df.dropna(subset=['review'])  # 리뷰컬럼에 비어있는 데이터 싹다 지우기

df['label'] = df['rating'].apply(
    lambda x: 'positive' if x >= 4 else 'negative'
)

## 만약에 람다로 작성하지 않을 경우
# def 라벨만들기(점수):
#     if 점수 >= 4:
#         return "positive"
#     else :
#         return 'negative'
# df['label'] = df['rating'].apply(라벨만들기)

print(df['label'].value_counts())

# =========================
# 3. 학습하기
# =========================
X = df['review']
y = df['label']

test_size = 0.1
random_state = 42

# X 데이터 y 정답
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=test_size,
    random_state=random_state
)

vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

acc = accuracy_score(y_test, model.predict(X_test_vec))
print(f"정확도 : {acc * 100 :.1f}")

# =========================
# 4. 모델 + 벡터라이터 저장
# digit 과 다른점 : digit 모델에서 학습한 결과만 저장하면 되지만
# 텍스트는 글자 → 숫자로 변환하여 분석하는 것이
# 어플에 작성된 리뷰 데이터들도 필요하기 때문에 벡터라이즈까지 함께 저장
# =========================

파일명 = f"review_model_{test_size}_{random_state}_{acc * 100:.1f}.pkl"

with open(파일명, 'wb') as f:
    pickle.dump({
        'model': model,
        'vectorizer': vectorizer
    }, f)

print(f"저장완료 {파일명}")
