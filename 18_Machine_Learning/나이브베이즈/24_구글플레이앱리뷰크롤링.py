"""
google-play-scraper
- 무료 2019 년에 출시된 도구
- 한국인이 만든 기술
구글 플레이 스토어 웹페이지를 대신 긁어와 주는 도구
외부 의존 없이 구글 플레이 스토어를 쉽게 크롤링할 수 있는 API 제공

pip install google-play-scraper 설치는 이렇게 작성하고
사용에는 _를 작성한다.
"""

from google_play_scraper import reviews, Sort
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

#  초기에 작성하는 코드는 구글 스크래퍼를 만든 개발자가 제공한 코드
result, _ = reviews(
    'com.kakao/talk',  # 구글 플레이 앱 ID
    lang='ko',
    country='kr',
    sort=Sort.NEWEST,
    count=500  # 500개 정도 수집하겠다.
)
# csv 저장 하고 라벨만든다음 데이터 쪼개고 모델 만들어서 결과 조회
df = pd.DataFrame(result)[['content', 'score']]  # [[]] = 표형태 [] = 표 하나
df.columns = ['review', 'rating']
df.to_csv('csvs/kakao_app_reviews.csv', index=False, encoding='utf-8-sig')
print(f"총 {len([df])}개 수집완료")
print(df.head())

# =================================================================
# 데이터 전처리는 시작된 상황
# 라벨 만들기 (무조건 해야하는 것이 아니라 개발자 분석가의 원하는 니즈에 맞춰서 할지 말지 결정
# 4~5 점 : positive 1~2점 : negative

df = df[df['rating'] != 3]  # df['rating'] 이 컬럼 에 존재하는 점수가 3일 때는 제거하고
# 3이 아닌게 맞다면 3이 아닌 데이터만 다시 df['rating'] 안에 넣겠다.

df['label'] = df['rating'].apply(
    #      if x >= 4 x 데이터가 4보다 크거나 같으면 'positive' 로 하고
    #      else 나머지는 'negative' 하겠다.
    # 위에서 3은 제거된 상태
    lambda x: 'positive' if x >= 4 else 'negative'
)
# =================================================================

# =================================================================
# 전처리 완료된 데이터를 train test 분리하여 모델 만들기
# X_train, X_test, y_train, y_test = train_test_split(df['review'], df['label'], test_size=0.2, random_state=42)


X = df['review']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vec, y_train)
print(f"정확도 : {model.score(X_test_vec, y_test):.4f}")
