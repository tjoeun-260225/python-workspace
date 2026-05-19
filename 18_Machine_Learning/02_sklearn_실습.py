import pandas as pd
# 집값예측 load_boston() -> 2023년 폐지됨 인종차별적 데이터가 있다하여 공식 제거
# 캘리포이나 집 예측
from sklearn.datasets import load_digits, load_wine, load_breast_cancer, load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def 속성_메서드_조회():
    """
    공통적으로 모두 있는 것
    'DESCR'         = 데이터 설명서 print(data.DESCR) 이 데이터가 뭔지 영어로 설명 나옴
    'data'          = 입력값(X에 넣는 학습용 데이터)
    'feature_names' = 컬럼 이름 data의 각 열이 무엇인지 컬럼이름
    'frame'         = pandas DataFrame 형태로 데이터 조회
                      DESCR 설명이 아닌 표 형태로 데이터를 보고 싶을 때 사용
     'target'       = 정답 (y에 넣는 것)
                      0, 1, 2 와 같이 index 숫자로 된 정답
     'target_names' = 정답 이름
                      0, 1, 2가 실제로 무엇인지 명칭이 기입
     'images'       = 손글씨에만 존재
     'data_module'  = 유방암에만 존재
                      내부적으로 데이터 어디서 가져왔는지 확인 개발자가 직접 사용할 일은 거의 없다.
     'filename'     = 데이터 파일이 컴퓨터 어디에 저장됐는지 경로
                      sklearn 을 이용해서 데이터를 가져올 때 유방암은 가져온 데이터가 어디있는지 확인할 수 있는 속성이 있다.

    손글씨 속성 & 메서드 : ['DESCR', 'data', 'feature_names', 'frame', 'target', 'target_names', 'images']
    와  인 속성 & 메서드 : ['DESCR', 'data', 'feature_names', 'frame', 'target', 'target_names']
    유밤암 속성 & 메서드 : ['DESCR', 'data', 'feature_names', 'frame', 'target', 'target_names', 'data_module', 'filename']
    """
    손글씨데이터관련기능 = load_digits()
    #print(f"손글씨 속성 & 메서드 : {dir(손글씨데이터관련기능)}")
    와인데이터관련기능 = load_wine()
    #print(f"와인 속성 & 메서드 : {dir(와인데이터관련기능)}")

    # 만약 wine 데이터를 frame 표 형태로 보기
    df = pd.DataFrame(와인데이터관련기능.data, columns=와인데이터관련기능.feature_names)
    print(df)

    유밤암데이터관련기능 = load_breast_cancer()
    #print(f"유밤암 속성 & 메서드 : {dir(유밤암데이터관련기능)}")
    # 이외 pandas 등 다른 모듈에서도 dir(모듈이 들어있는 변수공간의명칭) 작성하면
    # 내부에 어떤 속성과 메서드가 있는지 조회 가능

#속성_메서드_조회()


def 손글씨숫자분류():
    # 1. sklearn 에서 미리 수집하여 신입 개발자들에게 제공하는 손글씨 데이터 가져오기
    data_load = load_digits()  # 나중에는 개발자가 원하는 결과에 맞춰 데이터 수집하고 수집한 데이터 가져오기
    X = data_load.data  # 8x8 픽셀 이미지를 1줄로 편 숫자 64개 저장
    y = data_load.target  # 정답 (0~9)

    # 2. 학습용 / 테스트용 나누기 load_digits() = 총 1797개 에서 8:2 로 나눈 기준
    # X_train = 손     글     씨     데     이     터 1437개
    # X_test  = 각 손글씨 이미지에 해당하는 숫자  번호 1437개 정답으로 들어감
    # y_train = 손글씨 학습이 제대로 되었는지 확인용   데이터 360개
    # y_test  = 손글시 학습이 제대로 되었는지 채점용 숫자번호 360개
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. 모델 학습
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)

    # 4. 예측 & 정확도
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"정확도 : {acc * 100:.1f}%")


# 손글씨숫자분류()


def 와인등급분류():
    # 1. 데이터 불러오기
    data_load = load_wine()  # 제공한 기능에 어떤 속성 메서드가 있는지 모르겠다.
    X = data_load.data  # 알코올, 산도 등 13가지 성분
    y = data_load.target  # 정답 (0, 1, 2 등급)

    # 2. 학습용 / 테스트용 나누기 (전체 178개 → train 142 / test 36)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. 모델 생성 & 학습
    model = KNeighborsClassifier(n_neighbors=3) #
    model.fit(X_train, y_train)

    # 4. 예측 & 정확도
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"정확도 : {acc * 100:.1f}%")  # 약 70~75% 나오면 성공

#와인등급분류()

def 유방암분류():
    # 1. 데이터 불러오기
    data_load = load_breast_cancer()
    X = data_load.data  # 종양 크기, 모양 등 30가지 수치
    y = data_load.target  # 정답 (0: 악성, 1: 양성)

    # 2. 학습용 / 테스트용 나누기 (전체 569개 → train 455 / test 114)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=65)

    # 3. 모델 생성 & 학습
    """
    3이 딱히 정답은 아니나 관례상 3이나 5를 많이 사용
    
    n_neighbors=1   →  제일 가까운 1개만 보고 결정 / 너무 단순해서 틀릴 가능성 높음
    n_neighbors=3   →  3개 다수결 / 무난하게 잘 맞춤
    n_neighbors=5   →  5개 다수결 / 더 신중하게 결정
    n_neighbors=100 →  너무 많이봐서 오히려 정확도 떨어진다.
    ...    
    """
    model = KNeighborsClassifier(n_neighbors=3) # 관례상 3이나 5을 많이 사용
    model.fit(X_train, y_train)

    # 4. 예측 & 정확도
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"정확도 : {acc * 100:.1f}%")  # 약 94~96% 나오면 성공

# 유방암분류()

def 붓꽃데이터_csv_저장하기():
    붓꽃 = load_iris()

    df = pd.DataFrame(붓꽃.data, columns=붓꽃.feature_names)
    df['정답'] = 붓꽃.target
    df['정답이름'] = df['정답'].map({
        0: 'setosa',
        1: 'versicolor',
        2: 'verginica',
    })
    # index = False 맨 왼쪽에 0~3 번호 저장 안함
    df.to_csv("붓꽃.csv", index=False, encoding='utf-8-sig')
    print("저장완료")

붓꽃데이터_csv_저장하기()








