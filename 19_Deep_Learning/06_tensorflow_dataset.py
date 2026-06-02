"""
Scikit-learn
프랑스 국립정보자동화연구소
2007년 구글 Summer of Code 프로젝트에서 수상작
전세계 오픈소스 커뮤니티에서 함께 관리
회사 제품이 아니라 대회로 만들어진 순수 오픈소스

텐서플로우에서 제공하는 정제된 데이터셋
2015년 구글 Brain 팀 공개
Keras는 구글 엔지니에거 만들고, Tensorflow 부서에 합쳐짐

Google 은 남의 데이터나 남의 소스를 기생하여 본인의 프로젝트를 만드는 것 싫어한다.
Google 자체에서 데이터를 만들고, 자체에서 프로젝트를 만들자!

텐서플로우인데 우리도 데이터를 제공할게^^
MNIST             숫자분류   0~9 숫자 데이터
(사이킷런 load_digit() 숫자분류 모델이 있지만 구글은 자체적으로 만들고 배포하는 것 선호)
Fashion MNIST     옷  분류   10개 데이터셋
CIFAR-10          사진분류   10개 데이터셋
IMDB              감정분류   1개
Boston Housing    집값예측   1개            회귀 : mse

보통 분류는       마지막층에 몇 개의 분류가 나오고, softmax 많이 사용하며
                    Dense(분류개수, activation='softmax')
     예측(회귀는) 마지막층에 activation 없이 Dense 하나만 사용하기도 한다.
                    Dense(1)

loss 이미지 글자 예측 도 많이 사용하는 loss가 정해져 있다.
"""
import tensorflow as tf
from tensorflow.keras.datasets import mnist, fashion_mnist, california_housing
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Input, Flatten


# 1. MNIST - 손글씨 숫자
def 손글씨_딥러닝():
    # sklearn - 프랑스연구소에서 제공하는 데이터 셋과 데이터셋 훈련 / 테스트 용 분리 작업
    # X, y = load_iris(return_X_y=True)
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # tensorflow - 구글에서 제공하는 데이터 셋과 데이터셋 훈련 / 테스트 용 분리 작업
    # 머신러닝은 머신러닝이고 우리가 제공하는 딥러닝은 이렇게 사용해라~
    # 텐서플로우 구글 자체에서 권장하는 코드
    # 텐서플로우에서 제공하는 손글씨를 불러와 훈련용과 정답용으로 나누어 분리하기
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    """
    훈련 이미지 수 : 60000
    이미지 크기 : 28 x 28
    픽셀값 범위: 0 x 255
    
    255.0 = 이미지 데이터에서 주로 사용하는 표기법
    대부분의 이미지 데이터는 255.0 을 작업
    이미지 픽셀값은 원래 0 ~ 255 숫자
    
    #000000 = 완전 검정
    #ffffff = 완전 흰색  255 = f
    (0=완전검정, 255=완전흰색)
    
    X_train / 255.0 훈련 데이터도                           이미지 픽셀값에 맞춰 조절
    X_test / 255.0 훈련이 제대로 되었는지 확인하는 이미지도 이미지 픽셀값에 맞춰 조절
    딥러닝은 숫자가 너무 큰것을 싫어하기 때문에 255로 나눠서 0~1 사이로 맞춰주는 작업
    이미지 데이터 숫자들은 작은숫자로 정규화 작업 진행하는 것
    각각 정규화 한 데이터를 X_train에 다시 담고, X_test 에 다시 담아놓는다.
    """
    X_train, X_test = X_train / 255.0, X_test / 255.0

    # 로봇 뇌 만들기
    model = Sequential([
        # ❌❌❌❌❌❌❌❌❌❌
        # tensorflow.keras.layers.Dense(8, activation='relu', input_shape=(1,)),
        # tf.keras.layers.Dense(8, activation='relu', input_shape=(1,)),

        # AI가 위와 같은 코드를 제공한다면 레거시한 AI 모델이다.

        # 맨 위에
        # from tensorflow.keras.layers import Dense, Input, Flatten
        # 이 한줄만 작성하면 매번 tensorflow에서 keras에 있는 layers 내에 존재하는
        # Dense 이다 를 매번 작성하지 않아도 된다.
        # ⭕⭕⭕⭕⭕⭕⭕⭕⭕⭕
        Input(shape=(28, 28)),  # tensorflow 에서 28x28로 데이터 호출해서 사용하라 적힌대로 작성
        Flatten(),
        Dense(128, activation='relu'),
        Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  # 보통 이미지에서 loss 로 sparse_categorical_crossentropy 많이 사용
                  # loss = 정답 채점 방식
                  # binary              = O/X 문제 둘 중 하나 채점할 때 사용
                  # categorical        = 정답을 배열로 표시
                  # sparse_categorical = 정답을 숫자로 표시
                  loss='sparse_categorical_crossentropy',  # 강아지 고양이 개 1,2,3 나누어서 정답인 숫자 표현
                  metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=10, verbose=1, batch_size=32)

    """
    손글씨 훈련 데이터 : 60000 장
    epochs = 10               60,000 장 짜리 데이터를 처음부터 끝까지 읽는 것을 10번 반복
    수능EBS 수학책을 10회독 하는 것과 똑같은 것
    
    10회독을 할 때
    1회독 책 1권 160장 월요일 30장 화요일 30장 수요일 30장 목요일 30장 금요일 30장 토요일 10장
    ...
    총 10번 한다
    마지막에는 60000장 / 배치사이즈 32 = 1875 나뉜 나머지 313 장 공부하겠다.
    
    1875/1875
    313/313 
    """

    loss, acc = model.evaluate(X_test, y_test, verbose=1)
    print(f"[MNIST]정확도 : {acc * 100:.1f}%")


# 2. 옷 맞추기
def run_fashion_mnist():
    # Step 1. 데이터 불러오기
    (X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

    # Step 2. 정규화 - 픽셀값 0~255를 0~1로 바꾸기
    X_train, X_test = X_train / 255.0, X_test / 255.0

    # Step 3. 모델 설계
    model = Sequential([
        Input(shape=(28, 28)),
        Flatten(),
        # 보통 Dense 에서 숫자값은
        # 입출력층을 제외하고
        # 8 16 32 64 128 256 512 단위 형태로 많이 사용
        # 128 256 64 많이 사용
        Dense(256, activation='relu'),
        Dense(10, activation='softmax')
    ])

    # Step 4. 컴파일
    model.compile(
        optimizer='adam',  # 99.9 adam 사용
        loss='sparse_categorical_crossentropy',  # 이미지
        metrics=['accuracy']  # 확률 쓰지 않는 한 변하지 않는다.
    )

    # Step 5. 학습
    # 학습쪽에 epochs 나 batch_size 조절해서 정답률 높이기
    model.fit(X_train, y_train, epochs=30, verbose=1)

    # Step 6. 평가
    loss, acc = model.evaluate(X_test, y_test, verbose=0)
    print(f"[Fashion MNIST] 정확도: {acc * 100:.1f}%")


# 3. 집값 예측하기 - 윤리적인 문제로 인하여 sklearn 과 마찬가지로 사용 자제
def 캘리포니아집값예측():
    (X_train, y_train), (X_test, y_test) = california_housing.load_data()

    # sklearn 에서 했던 정규화 작업을 추가할 수 있다.
    # 방 개수 : 1 ~ 10            -3 ~ 3
    # 인구 수 : 100 ~ 35,000      -3 ~ 3
    # 집   값 : 0.1 ~ 5.0         -3 ~ 3
    # 각각의 최대최소를 이용하여 범위를 동일하게 맞추어 주는 것이 좋다.
    # 범위가 너~무 달라서 정규화가 없으면 Loss 크게 나온다.
    # StandardScaler 와 같은 기능을 이용해서  들쑥 날쑥 한 범위를 각 컬럼 속성에 맞게 통일

    model = Sequential([
        Input(shape=(8, 0)),  # tensorflow Docs에 8개의 컬럼으로 이루어져 있다 쓰여있다.
        Dense(64, activation='relu'),
        Dense(32, activation='relu'),
        Dense(1)
    ])

    model.compile(optimizer='adam', loss='mse')
    model.fit(X_train, y_train, epochs=50, verbose=1)
    loss = model.evaluate(X_test, y_test, verbose=1)
    print(f"캘리포니아 집값 예측 : {loss:.2f}%")
