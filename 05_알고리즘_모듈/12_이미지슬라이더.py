'''
pip install pillow
이미지 관련 모듈
'''
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from PIL.ImageOps import expand


class 이미지회전앱:
    def __init__(self, root):
        self.root = root
        self.root.title("이미지 회전기")
        self.root.geometry("700x620")
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(False, False)

        self.원본이미지 = None
        self.현재각도 = 0

        self.UI만들기()

    def UI만들기(self):
        # 제목
        tk.Label(self.root, text="이미지 회전기",
                 font=("맑은 고딕", 20, "bold"),
                 bg="#1a1a2e",
                 fg="#e94560"
                 ).pack(pady=(20, 10))

        # 캔버스
        self.캔버스 = tk.Canvas(
            self.root,
            width=480,
            height=360,
            bg="#0f3460",
            highlightthickness=0
        )
        self.캔버스.pack(pady=10)

        self.캔버스.create_text(
            240, 180,
            text="아래 버튼으로 이미지를 불러오세요.",
            fill="#a0a0c0",
            tags="안내"
        )
        # 버튼 ui
        버튼프레임 = tk.Frame(self.root, bg="#1a1a2e")
        버튼프레임.pack(pady=10)

        btn = {"font": ("맑은 고딕", 11, "bold"),
               "bg": "#e94560",
               "fg": "white",
               "relief": "flat",
               "cursor": "hand2",
               "padx": 16,
               "pady": 8,
               "bd": 0}
        프레임 = tk.Frame(self.root, bg="#1a1a2e")
        프레임.pack(pady=10)
        tk.Button(프레임, text="열기", command=self.이미지열기, **btn).grid(row=0, column=0, padx=8)
        tk.Button(프레임, text="왼쪽 90도", command=self.회전(-90), **btn).grid(row=0, column=1, padx=8)
        tk.Button(프레임, text="오른쪽 90도", command=self.회전(90), **btn).grid(row=0, column=2, padx=8)

        self.슬라이더 = tk.Scale(self.root,
                             from_=0,
                             to=360,
                             orient="horizontal",
                             length=400,
                             command=self.슬라이더회전,
                             bg="#1a1a2e",
                             fg="white",
                             troughcolor="#0f3460",
                             highlightthickness=0
                             )
        self.슬라이더.pack(pady=10)

        self.각도라벨 = tk.Label(self.root, text="현재 각도 : 0도", bg="#1a1a2e", fg="#e94560")
        self.각도라벨.pack()

    def 이미지열기(self):
        경로 = filedialog.askopenfilename(filetypes=[("이미지","*.png *.jpg *.jpeg *.bmp *.gif")])
        if 경로:
            self.원본이미지 = Image.open(경로)
            self.현재각도 = 0
            self.슬라이더.set(0)
            self.이미지표시(0)

    def 회전(self, 방향):
        if not self.원본이미지:return
        self.현재각도 = (self.현재각도 + 방향)  %360
        self.슬라이더.set(self.현재각도)
        self.이미지표시(self.현재각도)

    def 슬라이더회전(self,값):
        if not self.원본이미지: return
        #self.현재각도 = (self.현재각도 + 방향)
        self.현재각도 = int(값)
        self.이미지표시(self.현재각도)

    def 이미지표시(self,각도):
        img = self.원본이미지.rotate(-각도, expand=True)
        img.thumbnail((480, 360))
        self.tk이미지 = ImageTk.PhotoImage(img)
        self.캔버스.delete("all")
        self.캔버스.create_image(240,180, anchor="center", image=self.tk이미지)
        self.각도라벨.config(text=f"현재각도 : {각도}")

root = tk.Tk()
이미지회전앱(root)
root.mainloop()