"""
텍스트를 소리로 변환할 수 있다.
pip install gTTS pygame

google 번역기를 연동해서 텍스트를 음성으로 읽어주는 도구

"""
from gtts import gTTS
import pygame


# ① 공통 함수 완성하기
def tts재생(text):  # 매개변수 이름을 채우세요
    tts = gTTS(text=text, lang='ko')  # ② 매개변수 활용
    tts.save("output.mp3")

    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pass


def 문장읽기():
    text = "안녕하세요."
    pygame.mixer.init()
    tts재생(text)  # ③ 공통 함수 호출


def 텍스트파일읽기():
    f = open("read_me.txt", "r", encoding="utf-8")
    text = f.read()
    f.close()
    print(text)
    tts재생(text)  # ④ 공통 함수 호출 + 인자


def 입력한글자읽기():
    pygame.mixer.init()
    while True:
        text = input("읽을 문장을 입력하세요 (종료하려면 'q' 입력): ")

        if text == "q":
            print("종료합니다.")
            break

        tts재생(text)  # ⑤ 공통 함수 호출 + 인자


입력한글자읽기()
