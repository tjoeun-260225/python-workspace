import tkinter as tk

창 = tk.Tk()
창.title("계산기")
창.geometry("300x200")

tk.Label(창, text="숫자 1").grid(row=0, column=0, padx=10, pady=5)
숫자1 = tk.Entry(창, width=10)
숫자1.grid(row=0, column=1)

tk.Label(창, text="숫자 2").grid(row=1, column=0, padx=10, pady=5)
숫자2 = tk.Entry(창, width=10)
숫자2.grid(row=1, column=1)

결과 = tk.Label(창, text="결과:", font=("D2Coding", 14))
결과.grid(row=3, columnspan=2, pady=10)

def 계산기능():
    a = float(숫자1.get())
    b = float(숫자2.get())
    결과.config(text=f"결과 : {a + b}")

tk.Button(창, text="더하기",command=계산기능).grid(row=2,columnspan=2,pady=5)
창.mainloop()