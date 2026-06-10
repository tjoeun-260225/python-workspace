# 26_tkinter_ctype_yfinance_LSTM_주가예측

import yfinance as yf
import tkinter as tk


def get_price():
    tkinter = yf.Ticker("005930.KS")
    price = tkinter.fast_info.last_price
    label.config(text=f"삼성전자 : {price:,.0f}원")
    root.after(5000, get_price)  # 5초마다 가격 조회 반복


root = tk.Tk()
root.title("실시간 주가")
root.geometry("300x100")

label = tk.Label(root, text="로딩중...", font=('D2coding', 20))
label.pack(expand=True)
get_price()
root.mainloop()
