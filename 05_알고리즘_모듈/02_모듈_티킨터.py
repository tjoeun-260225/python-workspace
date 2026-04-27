'''
tkinter
- 파이썬으로 기본 GUI 를 만들수 있는 도구
- 파이썬 개발자가 만들어 기본으로 세팅되어 있는 도구

좀 더 예쁜 GUI 가 필요하다면
PyQt6 CustomTkinter 를 사용해도 된다.
'''
import tkinter as tk  # tkinter 가져올 것인데 이 이름이 너무 길기 때문에 tk 라는 이름으로 사용

window = tk.Tk()
window.title("내 첫 창")
window.geometry("400x300")  # 가로 x 세로 크기

# 텍스트 라벨   화면                             컴퓨터에 설치된 글꼴, 글꼴사이즈
label = tk.Label(window, text="안녕하세요!", font=("D2Coding", 20))
label.pack(pady=10)  # 내부 여백 상하 10씩 제공 / padx = 10 좌우 10씩 여백주기

# 입력 창
entry = tk.Entry(window, width=30)
entry.pack(pady=5)

def 버튼클릭():
    name = entry.get()
    label.config(text=f"안녕, {name}")

btn = tk.Button(window,text="클릭", command=버튼클릭)
btn.pack(pady=5)
# 맨 마지막에 작성
window.mainloop()  # 오른쪽 맨 위 에 있는 x 버튼을 클릭하기 전까지 프로그램을 계속 실행
