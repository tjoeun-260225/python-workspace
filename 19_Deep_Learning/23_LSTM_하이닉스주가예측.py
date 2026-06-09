import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, LSTM, Dense

# 1. 60일 치를 가져오는데 2020년 기준으로 60일 치를 가져오는 것이 맞을까?
# 2. 종가 → 종가 + 거래량 을 같이 넣게 되면 어떻게 될 것인가
# window = 60일치가 아니라 120일치를 가져오게 된다면?
# 3. LSTM 64 → 128 늘리는 것 과 같은 행위
df = pd.read_csv('SK하이닉스.csv', index_col=0, skiprows=[1, 2])
df.index = pd.to_datetime(df.index)
df.columns = ['Close', 'High', 'Low', 'Open', 'Volume']
close = df[['Close']] # df[['Close','Volume']]
print(close.tail())

scaler = MinMaxScaler()
scaled = scaler.fit_transform(close)
X, y = [], []
for i in range(60, len(scaled)):
    X.append(scaled[i - 60: i]) # 0 번부터 60일치의 데이터만 가져오겠다.
    y.append(scaled[i])
X, y = np.array(X), np.array(y)
print(X.shape)  # (날짜수, 60, 1)

split = int(len(X) * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

model = Sequential([
    # 종가(60, 1)            →  종가 + 거래량   (60, 2)
    # 종가(60, 1)            →  종가 + 거래량   (60, 2)
    # 60일치 ,종가           →  (60 , 1)
    # 120일치,종가           →  (120, 1)
    # 120일치,종가 + 거래량  →  (120, 2)
    Input(shape = (60, 1)),
    LSTM(64, return_sequences=True),
    LSTM(32),
    Dense(1)
])
# binary = 둘 중하나 선택
# sparse_categorical_crossentrophy = 세 개 이상 중 확률적으로 큰 분류 선택
# mse    = 예측
model.compile(optimizer='adam', loss='mse')
model.summary()

model.fit(X_train, y_train,
          epochs=20,
          batch_size=32,
          validation_split=0.1)

pred = model.predict(X_test)
pred_price = scaler.inverse_transform(pred)
real_price = scaler.inverse_transform(y_test)

plt.figure(figsize=(12, 5))
plt.plot(real_price, label='실제 주가')
plt.plot(pred_price, label='예측 주가')
plt.title('SK하이닉스 주가 예측 (LSTM)')
plt.legend()
plt.show()
