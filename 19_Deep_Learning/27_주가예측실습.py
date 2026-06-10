import yfinance as yf
import tkinter as tk
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Input

WINDOW = 10  # 과거 몇 개 봉 사용


# ── 모델 정의 ──────────────────────────────────────
def build_model(window):
    model = Sequential([
        Input(shape=(window, 1)),
        LSTM(64, return_sequences=True),
        LSTM(32),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model


# ── 모델 학습 ──────────────────────────────────────
def train_model():
    # 5분 봉은 60일치만 가능
    # 가져오는 데이터 interval 에 따라 period 설정할 수있는 기간이 다름
    df = yf.download("005930.KS", period="60d", interval="5m")
    prices = df['Close'].dropna().values.reshape(-1, 1)

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(prices)

    X, y = [], []
    for i in range(WINDOW, len(scaled)):
        X.append(scaled[i - WINDOW:i])  # 과거 WINDOW개
        y.append(scaled[i])  # 다음 1개

    X, y = np.array(X), np.array(y)

    model = build_model(WINDOW)
    model.fit(X, y, epochs=5, batch_size=16, verbose=0)

    return model, scaler, prices


# ── 5분 후 예측 ────────────────────────────────────
def predict_next(model, scaler, prices):
    last = prices[-WINDOW:].reshape(-1, 1)
    scaled = scaler.transform(last)
    X = scaled.reshape(1, WINDOW, 1)
    pred = model.predict(X, verbose=0)
    return scaler.inverse_transform(pred)[0][0]


# ── 현재가 갱신 ────────────────────────────────────
def get_price():
    ticker = yf.Ticker("005930.KS")
    price = ticker.fast_info.last_price
    current_label.config(text=f"현재가: {price:,.0f}원")
    root.after(5000, get_price)


# ── UI ────────────────────────────────────────────
root = tk.Tk()
root.title("삼성전자 실시간 + LSTM 예측")
root.geometry("320x180")

tk.Label(root, text="삼성전자 주가", font=('D2Coding', 14, 'bold')).pack(pady=5)

current_label = tk.Label(root, text="로딩중...", font=('D2Coding', 16))
current_label.pack()

pred_label = tk.Label(root, text="예측가: 학습중...", font=('D2Coding', 14), fg='blue')
pred_label.pack(pady=5)

status_label = tk.Label(root, text="", font=('D2Coding', 10), fg='gray')
status_label.pack()


# ── 실행 ──────────────────────────────────────────
def run():
    status_label.config(text="모델 학습중... 잠시만요")
    root.update()
    model, scaler, prices = train_model()
    pred = predict_next(model, scaler, prices)
    pred_label.config(text=f"5분 후 예측: {pred:,.0f}원")
    status_label.config(text="학습완료 ✓")


get_price()
root.after(100, run)
root.mainloop()
