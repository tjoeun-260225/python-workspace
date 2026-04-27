import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps

class 이미지회전앱:
    def __init__(self, root):
        self.root = root
        self.root.title("이미지 회전기")
        self.root.geometry("700x620")
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(False, False)

        self.원본이미지 = None
        self.현재각도 = 0
        self.반전여부 = False # TODO 3-1: 반전 상태 저장

        self.UI만들기()

    def UI만들기(self):
        tk.Label(self.root, text="이미지 회전기",
                 font=("맑은 고딕", 20, "bold"),
                 bg="#1a1a2e", fg="#e94560").pack(pady=(20, 10))

        self.캔버스 = tk.Canvas(self.root, width=480, height=360,
                             bg="#0f3460", highlightthickness=0)
        self.캔버스.pack(pady=10)
        self.캔버스.create_text(240, 180, text="아래 버튼으로 이미지를 불러오세요.",
                             fill="#a0a0c0", tags="안내")

        btn = {"font": ("맑은 고딕", 11, "bold"), "bg": "#e94560", "fg": "white",
               "relief": "flat", "cursor": "hand2", "padx": 16, "pady": 8, "bd": 0}

        프레임 = tk.Frame(self.root, bg="#1a1a2e")
        프레임.pack(pady=10)

        tk.Button(프레임, text="열기",        command=self.이미지열기,        **btn).grid(row=0, column=0, padx=8)
        tk.Button(프레임, text="왼쪽 90도",   command=lambda: self.회전(-90), **btn).grid(row=0, column=1, padx=8)
        tk.Button(프레임, text="오른쪽 90도", command=lambda: self.회전(90),  **btn).grid(row=0, column=2, padx=8)

        # TODO 1 & 2 & 3: 버튼 연결 완료
        tk.Button(프레임, text="저장", command=self.이미지저장, **btn).grid(row=0, column=3, padx=8)
        tk.Button(프레임, text="초기화", command=self.초기화, **btn).grid(row=1, column=0, padx=8, pady=8)
        tk.Button(프레임, text="↔ 좌우반전", command=self.좌우반전, **btn).grid(row=1, column=1, padx=8, pady=8)

        self.슬라이더 = tk.Scale(self.root, from_=0, to=360, orient="horizontal",
                             length=400, command=self.슬라이더회전,
                             bg="#1a1a2e", fg="white", troughcolor="#0f3460",
                             highlightthickness=0)
        self.슬라이더.pack(pady=10)

        self.각도라벨 = tk.Label(self.root, text="현재 각도: 0°",
                             bg="#1a1a2e", fg="#e94560",
                             font=("맑은 고딕", 11, "bold"))
        self.각도라벨.pack()

    def 이미지열기(self):
        경로 = filedialog.askopenfilename(
            filetypes=[("이미지", "*.png *.jpg *.jpeg *.bmp *.gif")])
        if 경로:
            self.원본이미지 = Image.open(경로)
            self.초기화() # 불러올 때 상태 리셋

    def 회전(self, 방향):
        if not self.원본이미지: return
        self.현재각도 = (self.현재각도 + 방향) % 360
        self.슬라이더.set(self.현재각도)
        self.이미지표시(self.현재각도)

    def 슬라이더회전(self, 값):
        if not self.원본이미지: return
        self.현재각도 = int(값)
        self.이미지표시(self.현재각도)

    def 이미지표시(self, 각도):
        # 1. 회전 적용 (expand=True는 이미지가 잘리지 않게 크기를 조절함)
        img = self.원본이미지.rotate(-각도, expand=True)

        # TODO 3-2: 좌우 반전 처리
        if self.반전여부:
            img = ImageOps.mirror(img)

        img.thumbnail((480, 360))
        self.tk이미지 = ImageTk.PhotoImage(img)
        self.캔버스.delete("all")
        self.캔버스.create_image(240, 180, anchor="center", image=self.tk이미지)
        self.각도라벨.config(text=f"현재 각도: {각도}° {'(반전됨)' if self.반전여부 else ''}")

    def 이미지저장(self):
        if not self.원본이미지: return
        경로 = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")])
        if 경로:
            # 현재 화면에 보이는 상태 그대로 저장용 이미지 생성
            img = self.원본이미지.rotate(-self.현재각도, expand=True)
            if self.반전여부:
                img = ImageOps.mirror(img)

            # TODO 1-1: 이미지 저장 실행
            img.save(경로)

    def 초기화(self):
        if not self.원본이미지: return
        # TODO 2: 모든 상태값 원복
        self.현재각도 = 0
        self.반전여부 = False
        self.슬라이더.set(0)
        self.이미지표시(0)

    def 좌우반전(self):
        if not self.원본이미지: return
        # TODO 3-3 & 3-4: 상태 토글 후 리프레시
        self.반전여부 = not self.반전여부
        self.이미지표시(self.현재각도)

root = tk.Tk()
이미지회전앱(root)
root.mainloop()