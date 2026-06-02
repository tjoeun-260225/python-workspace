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
from tensorflow.keras.datasets import mnist
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

    # 데이터 기본 정보 출력
    print(f"훈련 이미지 수 : {X_train.shape[0]}")
    print(f"이미지 크기 : {X_train.shape[1]} x {X_train.shape[2]}")
    print(f"픽셀값 범위: {X_train.min()} x {X_train.max()}")

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
        Input(shape=(28, 28)),  # tensorflow 에서 28x28로 데이터 호출해서 사용하라 적힌대로 작성
        Flatten(),
        Dense(128, activation='relu'),
        Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=10, verbose=1)
    loss, acc = model.evaluate(X_test, y_test, verbose=1)
    print(f"[MNIST]정확도 : {acc * 100:.1f}%")


손글씨_딥러닝()
