import os

"""
LSTM(LongShort-Term Memory)
기본RNN(=Vanilla RNN)은 이전 정보를 hidden state로 넘기는데
시퀀스가 길어질수록 기울기 소실 문제가 발생
기본 RNN의 경우
나는 어제 서울에서 밥을 먹었는데, 그 식당은 정말... [50단어 후] ... 맛있었다

50 스텝 전에 "서울" 이라는 단어를 기억하고 "맛있었다" 를 연결해야 하는데
RNN은 그 정보가 훈련 과정에서 사라진다.
LSTM 이걸 해결하기 위해 나타난 모델이다.

RNN  : h_t      = tanh(W∙[h_{t-1}, x_t] + b)
LSTM : h_t, C_t = LSTM(h_{t-1}, C_{t-1}, x_t)

이런식으로 내부 수학공식이 세부적으로 다르다.
C_t = 정보를 지울지 쓸지 읽을지와 같은 세 개의 게이트를 관통하며 결정 

SimpleRNN 의 향상된 버전 LSTM

"""
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding, Input
import tensorflow as tf
# 시계열 예측 예시
로봇뇌 = Sequential([
    # 레거시 모델 코드 하나를 써도 방법이 여러가지인데 너무 올드하다.
    # 키키키키키 → ㅋㅋㅋㅋㅋㅋ → ㅋㅎㅋㅎ
    # tf.keras.layers.LSTM(64, input_shape=("timesteps", "features"), return_sequences=True),
    # LSTM(64, input_shape=("timesteps", "features"), return_sequences=True),

    # 현재 가져온 모델을 기반으로 데이터 읽기를 시작하는 구조
    # 가장 최신 방식
    Input(shape=("timesteps", "features")),
    LSTM(64, return_sequences=True),
    LSTM(32),
    Dense(1)
])










