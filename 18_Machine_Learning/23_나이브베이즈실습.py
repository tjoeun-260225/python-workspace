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
