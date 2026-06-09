"""
기본적인 주식 용어 정리
가격 관련
시          가 - 그 날 장 시작할 때 첫 거래 가격
종          가 - 그 날 장 마감할 때 마지막 거래 가격(보통 예측 대상)
고가   /  저가 - 그 날 중 제일 높았던 / 낮았던 가격
전일      대비 - 어제 종가 대비 오늘 얼마나 올랐는지/내렸는지
52주 최고/최저 - 1년 중 제일 높았던/낮았던 가격

거래 관련
거    래    량 - 그 날 몇 주를 사고 팔았는가
거래      대금 - 거래량 X 가격 (총 얼마어치 거래되었는가)
호          가 - 사겠다 / 팔겠다 올려놓은 가격
   매수   호가 - 사려는 사람이 부른 가격
   매도   호가 - 팔려는 사람이 부른 가격

시장 관련
코    스    피 - 삼성전자, 현대차 같은 대형 기업이 모인 시장
코    스    닥 - 중소 / 벤처기업 위주 시장
상한가/하한가  - 하루에 오를 수 있는 최대 / 내릴 수 있는 최대

LSTM 으로 예측할 때 쓰는 것들

Close    종가   주로 이것으로 가격 예측
Open     시가   보조로 가끔 사용
High     고가   보조로 가끔 사용
Low      저가   보조로 가끔 사용
Volume 거래량   같이 넣으면 정확도 올라간다.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, LSTM, Dense


def 데이터불러오기(경로):
    # 아래 방법은 csv 를 가져올 때 가져올 컬럼과 행까지 한번에 전처리하여
    # csv 파일을 가져오는 방법
    # header    =  csv 파일에서 헤더가 두 가로줄 이상으로 나뉘어져 있을 때
    #             어디서부터 어디까지의 가로줄이 컬럼이다. 표기하는 방법
    #             거의 사용할 일 없다.
    # index_col = 0 첫 번째 컬럼(Date)를 인덱스로 사용할 때 표기
    #               안 쓰면 날짜가 그냥 일반 컬럼으로 사용된다.
    # skiprows = 2  쓸모없는 가로줄 제거 0,1,2 .... 에서 2에 해당하는 가로줄 제거
    # df = pd.read_csv(경로, header=[0, 1], index_col=0, skiprows=2)

    # samsung.csv 파일에서 날짜를 순번으로 사용하고, 가로 1번째줄, 2번째줄 제거
    # 의미없는 가로 두 줄 데이터이기 때문
    df = pd.read_csv(경로, index_col=0, skiprows=[1, 2])
    """
    row 0 번 째 Price,Close,High,Low,Open,Volume
    row 1 번 째 Ticker,005930.KS,005930.KS,005930.KS,005930.KS,005930.KS
    row 2 번 째 Date,,,,,
    
    skiprows=[1, 2]
    위 데이터에서 
    row 0 번 째 Price,Close,High,Low,Open,Volume 제외하고
    row 1 번 째와 row 2 번 째 를 제거하겠다.
    
    """
    df.index = pd.to_datetime(df.index)  # 위에서 선택한 인덱스를 날짜 형식 반환
    df.columns = ['Close', 'High', "Low", 'Open', "Volume"]  # 컬럼명 직접 지정
    return df[['Close']]  # 종가 컬럼만 가져와서 사용하겠다.


def 정규화(종가):
    스칼라 = MinMaxScaler()  # 0~1 변환기 생성
    스케일처리 = 스칼라.fit_transform(종가)  # 실제 0~1 로 변환
    return 스케일처리, 스칼라  # 변환한 데이터와 나중에 되돌릴 때 필요해서 스칼라도 반환


def 시퀀스만들기(데이터, window=60):
    X, y = [], []
    for i in range(window, len(데이터)):
        X.append(데이터[i - window:i])  # 60일치를 훈련 데이터로 넣고
        y.append(데이터[i])  # 그 다음날 정답 예측
    return np.array(X), np.array(y)


def 학습_테스트_모델분리(X, y, 분류기준=0.8):
    분리하기 = int(len(X) * 분류기준)  # 전체의 80% 가 되는 개수 확인 총데이터수 0.8
    # X_train에는 0에서부터 80% 데이터를 넣고
    # X_test 에는 81   부터 20% 데이터를 모두 가져오겠다.
    X_train, X_test = X[:분리하기], X[분리하기:]  # 앞 80% 학습용 / 뒤 20% 테스트용 사용
    y_train, y_test = y[:분리하기], y[분리하기:]  # 앞 80% 학습용 / 뒤 20% 테스트용 사용
    return X_train, X_test, y_train, y_test


# 힌트: Sequential 안에 Input → LSTM(64, return_sequences=True) → LSTM(32) → Dense(1) 순서
# 힌트: compile 은 optimizer='adam', loss='mse'
def 모델만들기(window=60):
    model = Sequential([
        Input(shape=(window, 1)),  # 입력 60일  종가 컬럼1개
        LSTM(64, return_sequences=True),
        LSTM(32),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    model.summary()
    return model


# 힌트: model.fit() 사용
# 힌트: epochs=20, batch_size=32, validation_split=0.1
def 학습하기(model, X_train, y_train):
    model.fit(X_train, y_train,
              epochs=20,
              batch_size=32,
              validation_split=0.1)
    return model


# 힌트: model.predict() 로 예측
# 힌트: 예측값이 0~1 이라서 스칼라.inverse_transform() 으로 실제 주가로 되돌려야 함
def 예측하기(model, X_test, y_test, 스칼라):
    예측 = model.predict(X_test)
    예측주가 = 스칼라.inverse_transform(예측)
    실제주가 = 스칼라.inverse_transform(y_test)
    return 예측주가, 실제주가


# 힌트: plt.figure(figsize=(12, 5))
# 힌트: plt.plot() 두 번 — 실제주가, 예측주가
# 힌트: plt.legend() 로 범례 표시
def 그래프그리기(실제주가, 예측주가):
    plt.figure(figsize=(12, 5))
    plt.plot(실제주가, label='실제 주가')
    plt.plot(예측주가, label='예측 주가')
    plt.title('삼성전자 주가 예측 (LSTM)')
    plt.legend()
    plt.show()


# 힌트: 위에서 만든 함수들을 순서대로 연결
종가 = 데이터불러오기('samsung.csv')
스케일처리, 스칼라 = 정규화(종가)
X, y = 시퀀스만들기(스케일처리, window=60)
X_train, X_test, y_train, y_test = 학습_테스트_모델분리(X, y)
model = 모델만들기()
model = 학습하기(model, X_train, y_train)
예측주가, 실제주가 = 예측하기(model, X_test, y_test, 스칼라)


# 그래프그리기(실제주가, 예측주가)


def 내일주가예측(종가, 스칼라, model, window=60):
    # 가장 최근 60일 데이터 꺼내기
    최근60일 = 종가.values[-window:]
    # 0~1 정규화
    최근60일_스케일처리 = 스칼라.transform(최근60일)
    # shape 변환 (60, 1)   (1,60,1) 변환  LSTM 입력 형식
    입력 = 최근60일_스케일처리.reshape(1, window, 1)
    # 예측
    예측 = model.predict(입력)
    # 내일주가 스케일러 되돌리기
    내일주가 = 스칼라.inverse_transform(예측)

    print(f"내일 예측 주가 : {내일주가[0][0]:,.0f}원")
    return 내일주가


내일주가예측(종가, 스칼라, model)

"""
Model: "sequential"
┌─────────────────────────────────┬────────────────────────┬───────────────┐
│ Layer (type)                    │ Output Shape           │       Param # │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ lstm (LSTM)                     │ (None, 60, 64)         │        16,896 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ lstm_1 (LSTM)                   │ (None, 32)             │        12,416 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense (Dense)                   │ (None, 1)              │            33 │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 29,345 (114.63 KB)
 Trainable params: 29,345 (114.63 KB)
 Non-trainable params: 0 (0.00 B)
Epoch 1/20                                학습데이터오차     검증 데이터 오차
32/32 ━━━━━━━━━━━━━━━━━━━━ 3s 36ms/step - loss: 0.0073 - val_loss: 0.0024
Epoch 2/20
32/32 ━━━━━━━━━━━━━━━━━━━━ 1s 26ms/step - loss: 9.0532e-04 - val_loss: 0.0018
Epoch 3/20
32/32 ━━━━━━━━━━━━━━━━━━━━ 1s 27ms/step - loss: 6.2545e-04 - val_loss: 0.0017
Epoch 4/20
32/32 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 6.2094e-04 - val_loss: 0.0017
Epoch 5/20
32/32 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 5.6094e-04 - val_loss: 0.0016
Epoch 6/20
32/32 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 5.4479e-04 - val_loss: 0.0016
Epoch 7/20
32/32 ━━━━━━━━━━━━━━━━━━━━ 1s 26ms/step - loss: 5.3405e-04 - val_loss: 0.0014
Epoch 8/20
32/32 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 4.9651e-04 - val_loss: 0.0014
Epoch 9/20
32/32 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 4.9028e-04 - val_loss: 0.0012
Epoch 10/20
32/32 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 4.6864e-04 - val_loss: 0.0012
Epoch 11/20
32/32 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 4.9366e-04 - val_loss: 0.0011
Epoch 12/20
32/32 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 4.8383e-04 - val_loss: 0.0011
Epoch 13/20
32/32 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 4.1698e-04 - val_loss: 0.0012
Epoch 14/20
32/32 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 3.9485e-04 - val_loss: 9.6016e-04
Epoch 15/20
32/32 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 3.7666e-04 - val_loss: 9.0117e-04
Epoch 16/20
32/32 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 3.6163e-04 - val_loss: 8.9677e-04
Epoch 17/20
32/32 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 4.1309e-04 - val_loss: 8.7992e-04
Epoch 18/20
32/32 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 3.7478e-04 - val_loss: 8.3275e-04
Epoch 19/20
32/32 ━━━━━━━━━━━━━━━━━━━━ 1s 24ms/step - loss: 3.4856e-04 - val_loss: 8.2842e-04
Epoch 20/20
32/32 ━━━━━━━━━━━━━━━━━━━━ 1s 25ms/step - loss: 3.5056e-04 - val_loss: 7.9769e-04
9/9 ━━━━━━━━━━━━━━━━━━━━ 0s 33ms/step

종료 코드 0(으)로 완료된 프로세스


"""
