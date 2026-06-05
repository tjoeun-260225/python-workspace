import os

"""
CNN = Convolutional Neural Network(합성곱 신경망)
사람의 눈이 사진을 보는 방식을 컴퓨터로 흉내낸 것

사람이 고양이 사진을 볼 때 → 귀, 수염, 눈을 보고 고양이다! 라고 알아채는 것처럼
CNN도 똑같이 작동한다.

이미지는 컴퓨터에게 무엇인가?
컴퓨터를 숫자 격자로 본다
고양이 사진(3x3 사진 크기가 있다)
[[255,200,180,], [210,190,170], [180,160,140]]
각 숫자 = 픽셀밝기(0=검정, 255=흰색) # ffffff = 255 255 255 와 같은 255 로 이루어진 흰색
컬러 사진 = R(빨강), G(초록), B(파랑) 3개 층

Conv2D = 특징을 찾는 돋보기
- 이미지에서 특징(feature) 을 찾는 필터
마치 돋보기로 사진을 훑는 것처럼, 작은 창문(필터)이 이미지 위를 쭉 지나가면서 특징 찾기
사진을 보고 사진 특징을 컬럼으로 정리하겠다.
필터가 찾은 것들 : 
    첫 번째 레이어 : 선,점, 경계선 같은 단순한 것들
    두 번째 레이어 : 귀, 모양, 눈 같은 복잡한 것들
    마 지막 레이어 : 이건 고양이다, 이건 자동차다 와 같은 결론
    Conv2D(64,(3,3))
    (3,3) 이란 3x3 과 같은 작은 창문 크기로 이미지 위를 전체 돌아다니며 특징찾는다.
    3x3 크기의 이미지 탐색은 왼쪽 → 오른쪽, 위 → 아래로 훑으면서 특징 찾는다.
    1x1 아주 작음 미세하게 탐색
    3x3 가장 많이 사용 평균적으로 미세하게 너무 크지도 않게 탐색
    5x5 더 넓게 봄
    7x7 아무 넓게 본다.
"""

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Input

# 사진을 확인하고 분류하는 로봇 뇌 만들기
#        뇌 만들기 시작
로봇뇌 = Sequential([
    # 가장 먼저 사물을 보는 로봇 눈 만들기 로봇의 눈은 사진이 흑백인지 사진 사이즈는 어떻게 되는지 생성
    Input((32, 32, 3)),
    # Input((32, 32, 1)), 흑백 사진 의 경우 초록 파랑 빨강이 필요 없으므로 1로 작성
    Conv2D(32, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2,2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')

    # 아래 방식은 모델 보겠다 와 모델 분석하는 신경층 만드는 것을 동시에 진행한 것
    # 레거시 방법
    # Conv2D(32,  (3, 3),  activation='relu',  input_shape=(32, 32, 3) )
])

# 로봇뇌 학습 준비

로봇뇌.compile(
    optimizer='adam', # 틀린 방법에 대하여 어떻게 오답노트를 작성할지 학습방법 선택
    # 학습방법은 난다 긴다하는 수학가이자 개발자들이 작성한 대표적인 공식들 중 하나 보통 사용
    loss='sparse_categorical_crossentrophy', # 틀린 정도 측정 3개 이상은 옆에 있는 loss 많이 사용
    metrics=['accuracy'] # 정확도 측정
)

#로봇뇌의 구조를 보는 메서드
로봇뇌.summary()
