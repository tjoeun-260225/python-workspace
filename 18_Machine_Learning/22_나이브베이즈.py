"""
나이브베이즈(Naive Bayes)
- 이 데이터가 어떤 클래스일 확률일 가장 높은가? 를 조건부 확률로 계산하는 분류 알고리즘
- Naive = 단순한 / 세상 물정 모르고 단순하게 생각한다 가정한다 의미
- Bayes = 사람 이름 18세기 영국 수학자 이름에서 따옴
           토마스 베이즈라는 사람이 만든 베이즈 정리를 사용해서 확률로 계산함
           베이즈 정리 : 새로운 증거가 생기면, 기존 믿음을 업데이트해서 참고하자

           스팸 | "무료" 등장 = ("무료"|스팸)  x (스팸)
                              --------------------------
                                       무료

        스팸 | "무료"        =     무료를 봤을 때 스팸일 확률          → 우리가 원하는 결과
        ("무료"|스팸)        =     스팸 메일에서 "무료" 가 등장할 확률 → 학습 데이터로 계산
        스         팸        =     전체 메일 중 스팸 비율             → 학습 데이터로 계산
        무         료        = 전체 메일에서 무료 등장 비율


예) 스팸 메일
이메일에 무료 당첨 이라는 단어가 있으면 스팸인가요?!
스팸일확률 = (스팸 메일 중 "무료" 가 포함된 비율) X (스팸 메일 중 "당첨" 이 포함된 비율) X (전체 스팸 비율)

각 단어가 서로 독립적이고 가정(naive)하고 곱해서 계산하는게 포인트

실제 사람들이 작성하는 문서 문장에는 단어들이 서로 연관되어 있지만, 나이브 베이즈는 "모두 독립적이다"
라고 단순하게 가정한다.
틀린 가정일 수 있지만 실제로 꽤 잘 작동하는 알고리즘
"""
import pandas as pd
# 나이브베이즈 기초 코드
from sklearn.naive_bayes import MultinomialNB  # 확률 학습하는 기능
from sklearn.feature_extraction.text import CountVectorizer  # 단어를 숫자로 변환하는 기능
from sklearn.model_selection import train_test_split

"""
코드 흐름 정리
            텍스트 데이터
                  ↓  CountVectorizer      단어를 숫자로
            숫자 행렬
                  ↓  MultinomialNB.fit()  확률 학습
            학습된 모델
                  ↓  predict()
            스팸 / 정상
나이브 베이즈 를 사용하면 좋은 데이터
스팸 분류
감정 분석(긍정/부정)
뉴스 카테고리 분류
XXX 이미지 분류 , 연속적인 숫자 데이터 추천하지 않는다.
"""


def 기초코드문법():
    # 1. 학습 데이터
    # 모든 이메일 데이터를 수집했다는 가정

    emails = [
        "무료 당첨 축하합니다",  # 스팸
        "무료 쿠폰 지금 받기",  # 스팸
        "내일 회의 자료 보내줘",  # 정상
        "프로젝트 일정 확인해줘",  # 정상
        "당첨 선물 무료 증정",  # 스팸
    ]

    labels = ["스팸", "스팸", "정상", "정상", "스팸"]

    # 2. 텍스트 → 숫자 변환 (단어 등장 횟수 세기)
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(emails)  # fit_transform 모델 데이터만 변환 작업할 것
    """
    train_test_split 데이터를 학습용과 정답용으로 나누고 랜덤섞기 기능을 작성하지 않은 이유
    train_test_split = 데이터를 학습용/테스트용 나누는 도구
    5개를 또 나누면 학습 데이터가 너~무 적어서 모델이 제대로 학습을 할 수가 없다.
    개념 설명용이라 그냥 학습에 모두 사용한 것
    
    train_test_split
    - 데이터가 100개 이상일 때 사용
    - 데이터가 100개 이하면 사실 너무 데이터가 적어서 의미가 크게 있진 않다.
    - SNS Spam(5572개) 필수로 사용해야 한다.
    
    
    
    
    """

    # 3. 모델 학습
    model = MultinomialNB()
    model.fit(X, labels)

    # 4. 새 이메일 예측
    new_email = ["무료 선물 당첨"]
    X_new = vectorizer.transform(new_email)
    result = model.predict(X_new)
    print(f"예측 결과 : {result[0]}")


def csv_기초코드문법():
    # 1. 깔끔하게 정제되어 공부하기 좋은 csv 파일 불러오기
    df = pd.read_csv(
        "csvs/spam_sms.csv",
        encoding='latin-1',
        usecols=[0, 1]  # usecols = 사용할 컬럼 선택 v1,v2, , ,
        #       v1,v2 컬럼만 사용하겠다.
    )

    # 2. v1, v2 라는 컬럼 이름을 명확하게 재정의 하고싶다.
    df.columns = ['label', 'message']

    # 3. 데이터 파일 조회
    print(df.head())
    print(df.shape)  # (5572, 2)
    print(df['label'].value_counts())

    """
           label message
        0   ham  Go until jurong point, crazy.. Available only ...
        1   ham                      Ok lar... Joking wif u oni...
        2  spam  Free entry in 2 a wkly comp to win FA Cup fina...
        3   ham  U dun say so early hor... U c already then say...
        4   ham  Nah I don't think he goes to usf, he lives aro...
        (5572, 2)
        
        df['label'].value_counts() 를 이용해서 라벨에서 ham 총 개수 spam 총 개수
        label    
        ham     4825
        spam     747
        Name: count, dtype: int64
    
    """

    # 4. 학습을 하기 위하여 데이터 분리
    X_train, X_test, y_train, y_test = train_test_split(
        df['message'],
        df['label'],
        test_size=0.2,
        random_state=42
    )

    vectorizer = CountVectorizer()

    '''
    MultinomialNB() -> 숫자로 정렬된 데이터를 기반으로 학습을 진행하도록 설계되어 있는 모델
    ValueError: Expected a 2-dimensional container but got <class 'pandas.Series'> instead. Pass a DataFrame containing a single row (i.e. single sample) or a single column (i.e. single feature) instead.
    
    MultinomialNB 를 사용하려면 반드시 CountVectorizer() 기능을 이용해서 글자 → 숫자 변환하는 작업을 해준다음 모델을 쓸 수 있다.
    
    '''

    X_train_숫자로변경 = vectorizer.fit_transform(X_train) # fit_transform = 훈련용 데이터만 선택해서
    #X_test_숫자로변경 = vectorizer.transform(X_train)
    """
    ValueError: Found input variables with inconsistent numbers of samples: [1115, 4457]
    위에서 분리한 테스트 데이터의 정답은 1115개 인데, 왜 테스트용 데이터라고 가져온건 4457개니?
    제대로 테스트 데이터 정답과 테스트용 데이터 선택해서 가져온 거 맞니?
    """
    X_test_숫자로변경 = vectorizer.transform(X_test)      # transform = 훈련이 제대로 됐는지 확인된 데이터만 선택해서

    # CountVectorizer() 기능 자체가 훈련용 데이터인가 훈련이 제대로 되었는지 테스트용 데이터인지 선택하여
    # 글자 → 숫자 화 처리한다.


    model = MultinomialNB()  # 모델 불러오기
    # model.fit(X_train, y_train)
    model.fit(X_train_숫자로변경, y_train)
    # print(f"정확도{model.score(X_test, y_test):.4f}")
    print(f"정확도{model.score(X_test_숫자로변경, y_test):.4f}")


csv_기초코드문법()
