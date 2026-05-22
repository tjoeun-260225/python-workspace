"""
데이터셋 분석 / 분류

IMDB 영화 리뷰 분석
5만 개의 영화 리뷰로 구성된 데이터 셋
Kaggle 대회에 존재
긍정/부정으로 되어 있어 나이브 베이즈로 텍스트 분류 공부를 하기 좋은 데이터셋

Fake News 가짜 뉴스 분류 데이터 셋
-> 난이도 중
"""

import pandas as pd
import requests
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split


# CountVectorizer 하는 일 관찰하기
def CountVectorizer기능():
    vectorizer = CountVectorizer()

    문장들 = [
        'I love this movie',
        'I hate this movie',
        'I love love this this this movie',
    ]

    결과 = vectorizer.fit_transform(문장들)
    '''
    vectorizer.fit_transform(문장들) 에서 일어나는 일들 
    1. 문장들에서 단어 목록을 분석한다. 중복은 제거한다.
    단어목록 → [I love this movie  hate]
    알파벳 순서로 정렬
    hate love movie this
    I가 사라진 이유는  CountVectorizer 가 단어 목록에서 1글자 단어는 자동으로 무시한다.
    2. 다시 문장들에서 각 단어들이 몇 번 출현했는지 숫자로 변환
    'I love this movie'              → 'hate love movie this'  ---> [0 1 1 1]
    'I hate this movie'               → 'hate love movie this'  ---> [1 0 1 1]
    'I love love this this this movie'→ 'hate love movie this'  ---> [0 2 1 3]
    '''
    print(결과.toarray())
    """
    [
    [0 1 1 1]
    [1 0 1 1]
    ]
    """


def csv_영화리뷰():
    # ================================
    # 1. 데이터 불러오기
    # ================================
    df = pd.read_csv("csvs/IMDB_Dataset.csv")

    # TODO 1: 데이터 상위 5개 출력해보기
    print(df.head())
    # TODO 2: 데이터 shape 출력 (몇 행 몇 열?)
    print(df.shape)
    # TODO 3: sentiment 컬럼 값 개수 출력 (positive 몇개, negative 몇개?)
    print(df['sentiment'].value_counts())

    # ================================
    # 2. 데이터 분리
    # ================================
    X = df['review']
    y = df['sentiment']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # ================================
    # 3. 텍스트 → 숫자 변환
    # ================================
    vectorizer = CountVectorizer()  # 숫자 배열기능()
    """
    vector = 배열이다.
    ize = ~로 만들다
    r = 도구
    vectorizer = 텍스트를 숫자 배열로 만들어주는 도구가 담긴 상자다. 변수 공간이다.
    
    배열 유사단어들이 많고, 상황에 따라 더 많이 불리고 사용되는 단어가 있을 뿐이다.
    array
    - 여러 개 담는 통
    
    vector
    - 수학에서 온 개념 방향과 크기를 가진 배열
    - 머신러닝에서는 단어를 숫자로 표현한 배열을 벡터라고 부른다.
     - array 보다는 vector 더 많이 단어로 선택해서 사용
     
    악어
    크로커다일 = 주둥이 v 자 이빨보이며 공격적이고 강 바닷물 어디서든 살 수 있다.
    앨리게이터 = 주둥이 u 자 이빨 안 보임 온순 강이나 늪에서만 서식
    
    강 근처에서 악어를 보는 사람들은 크로커다일 대신 앨리게이터라고 악어를 주로 부름
    
    바다 근처에서 악어를 보는 사람들은 크로커다일로 악어를 주로 부름
    """
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # ================================
    # 4. 모델 학습
    # ================================
    model = MultinomialNB()

    # TODO 9: 모델 학습시키기
    model.fit(X_train_vec, y_train)

    # ================================
    # 5. 정확도 확인
    # ================================

    # TODO 10: 정확도 출력 (소수점 4자리)
    # 어떤 때는 acc = model.score(X_test_vec,y_test) 을 넣어서 사용하고
    # 어떤 때는 바로 출력
    # 정확도를 사용할일이 여러번 있을 경우 acc 사용이 맞으나 아래와같이 1회성으로 확인만 한다면
    # print 내에 1회만 표기하는 것이 맞다.
    print(f"정확도: {model.score(X_test_vec, y_test):.4f}")

    # ================================
    # 6. 직접 예측해보기
    # ================================

    # TODO 11: 아래 리뷰 두 개를 벡터로 변환 후 예측 출력
    my_reviews = [
        "This movie was absolutely amazing. I loved every moment of it!",
        "Terrible movie. Boring and waste of time. I hated it."
    ]

    # TODO 12: my_reviews 를 벡터로 변환 (힌트: transform)
    my_vec = vectorizer.transform(my_reviews)  # 훈련이 아니라 test 이기 때문에 fit_transform 이 아닌
    # transform 만 사용해서 만들어진 예측모델이 제대로 동작하는지 테스트

    # TODO 13: 예측 결과 출력
    result = model.predict(my_vec)
    print(f"리뷰1 예측: {result[0]}")  # → positive
    print(f"리뷰2 예측: {result[1]}")  # → negative


def API_CSV_데이터수집():
    """
    데이터를 인터넷에서 수집하고 수집한 데이터를 csv 로 저장한다.
    데이터 수집에서 사용하는 사이트
    omdbapi.com
    api key free 발급 받아 사용 가능
    하루 1000번 무료 호출 가능
    """


# ==========================
# 1. API key setting
# ==========================
API_KEY = '6fae13d2'
영화목록 = ["Inception", "Titanic"]
data = []

def get_movie(title):
    #      http://www.omdbapi.com/?t=Avatar
    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
    """
    {"Title":"Avatar",
    "Year":"2009",
    "Rated":"PG-13",
    "Released":"18 Dec 2009",
    "Runtime":"162 min",
    "Genre":"Action, Adventure, Fantasy",
    "Director":"James Cameron",
    "Writer":"James Cameron",
    "Actors":"Sam Worthington, Zoe Saldaña, Sigourney Weaver",
    "Plot":"A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
    "Language":"English, Spanish",
    "Country":"United States, United Kingdom",
    "Awards":"Won 3 Oscars. 91 wins & 131 nominations total",
    "Poster":"https://m.media-amazon.com/images/M/MV5BMDEzMmQwZjctZWU2My00MWNlLWE0NjItMDJlYTRlNGJiZjcyXkEyXkFqcGc@._V1_SX300.jpg",
    "Ratings":[{"Source":"Internet Movie Database","Value":"7.9/10"},{"Source":"Rotten Tomatoes","Value":"81%"},{"Source":"Metacritic","Value":"83/100"}],
    "Metascore":"83",
    "imdbRating":"7.9",
    "imdbVotes":"1,486,308",
    "imdbID":"tt0499549",
    "Type":"movie",
    "DVD":"N/A",
    "BoxOffice":"$785,221,649",
    "Production":"N/A",
    "Website":"N/A",
    "Response":"True"}
    
    """
    response = requests.get(url)
    return response.json()  # omdbapi 접속해서 해당 제목의 영화 데이터 영화데이터 접근 권한 = api key  이용해서
    #  json 데이터 갖고오기



def csv_저장하기():
    for 제목 in 영화목록:
        영화사이트_데이터 = get_movie(제목)  # 위에서 만들어준 get_movie 기능에 제목을 하나씩 전달하여 검색하기 기능

        if 영화사이트_데이터.get("Response") == "True":
            data.append({
                "title": 영화사이트_데이터.get("Title"),
                "year": 영화사이트_데이터.get("Year"),
                "genre": 영화사이트_데이터.get("Genre"),
                "plot": 영화사이트_데이터.get("Plot"),
                "rating": 영화사이트_데이터.get("imdbRating"),
                "awards": 영화사이트_데이터.get("Awards"),
            })
            print(f"수집완료 : {제목}")

    df = pd.DataFrame(data)
    df.to_csv("csvs/omdb_movies.csv", index=False, encoding="utf-8-sig")
    print(f"\n 총 {len(df)}개 저장완료")
    print(df.head())


def 라벨만들기(df):
    df['label'] = df['rating'].astype(float).apply(
        lambda x: 'good' if x >= 8.0 else 'bad'
    )
    print(df[['title', 'rating', 'label']])
    return df


# ================================
# csv_불러오기()
# df['컬럼이름']
# ================================
def csv_불러오기():
    df = pd.read_csv("csvs/omdb_movies.csv")
    print('상위 5개 데이터 확인 : ', df.head())
    print('특정 컬럼 조회 : ', df['rating'])
    return df


# ================================
# 나이브 베이즈 학습
# ================================
def 나이브베이즈_학습(df):
    X = df['plot']
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    vectorizer = CountVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = MultinomialNB()
    model.fit(X_train_vec, y_train)

    print(f"정확도: {model.score(X_test_vec, y_test):.4f}")
    return model, vectorizer


# ================================
# 직접 예측
# ================================
def 직접예측(model, vectorizer):
    my_plots = [
        "A thief who enters dreams to steal secrets",
        "A boring love story with no action or excitement",
    ]
    my_vec = vectorizer.transform(my_plots)
    result = model.predict(my_vec)

    print(f"줄거리1 예측: {result[0]}")  # → good
    print(f"줄거리2 예측: {result[1]}")  # → bad


# ================================
# 실행
# ================================
csv_저장하기()
df = csv_불러오기()
df = 라벨만들기(df)
model, vectorizer = 나이브베이즈_학습(df)
직접예측(model, vectorizer)


# 1. 우리 회사에서 고객의 의견을 확인하는 모델로 사용
# 2. 특정영화를 여러 사이트 방문해서 사람들의 인지도가 어떤지 조회 분석
# 3. 맛집       여러 사이트를 방문해서 특정 지역에서 인지도 좋은 맛집 분석
# 4. 쇼핑... 논문 등 글자로 무언가를 파악해야할 때 사용