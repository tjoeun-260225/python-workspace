"""
텍스트를 소리로 변환할 수 있다.
pip install gTTS pygame

google 번역기를 연동해서 텍스트를 음성으로 읽어주는 도구

"""

from gtts import gTTS
import pygame


def 문장읽기():
    text = "안녕하세요."
    tts = gTTS(text=text, lang='ko')
    # txt 파일과 같은 글자 데이터를 읽을 수 있다.
    # lang='나라코드' 나라코드를 설정해주면 해당 나라에 발음과 형식에 맞추어 읽혀진다.
    # 없는 나라의 코드의 경우 실행 자체 안됨
    tts.save("hello.mp3")  # 글자를 소리로 변환하여 나의 컴퓨터 저장

    # pygame 재생
    pygame.mixer.init()  # 변환된 소리를 재생하기 위하여 소리 도구 준비
    pygame.mixer.music.load("hello.mp3")  # 소리낼 파일 준비
    pygame.mixer.music.play()  # 소리 재생 시작

    # 트릭
    # 소리를 내는 것보다 코드가 종료되는 속도가 더 빠르다.
    # get_busy() -> 현재 소리를 내고 있는 상황이 맞는가? True False 실시간으로 계속 감지하여
    # 소리가 끝날때까지 특정 코드를 멈추지 않고 실행하게 도와주는 기능
    # 모든 소리가 재생되고 나면 False가 되고 프로그램은 종료된다.
    while pygame.mixer.music.get_busy():
        pass  # 자바의 경우 while True{} 기능을 작성하지 않으면 그만이지만
    # 파이썬의 경우 :을 작성하면 무조건 : 아래에서 수행할 코드를 하나 무조건 작성
    # 작성할 것은 없지만 : 과 같은 기능 형식을 작성해야할 때
    # pass 작성해서 실행한다.

    # 특정 텍스트를 읽는 정도는 ai를 사용하지 않아도 읽을 수 있다.


def 텍스트파일읽기():
    # TODO: read_me.txt 파일 열기
    f = open("read_me.txt", "r", encoding="utf-8")  # 파일이름, 읽기모드, 한글깨짐방지
    text = f.read()  # 전체 내용 읽기
    f.close()

    print(text)

    tts = gTTS(text=text, lang='ko')
    tts.save("text.mp3")

    # 나머지 pygame 채워보기
    pygame.mixer.init()  # 변환된 소리를 재생하기 위하여 소리 도구 준비
    pygame.mixer.music.load("text.mp3")  # 소리낼 파일 준비
    pygame.mixer.music.play()  # 소리 재생 시작
    while pygame.mixer.music.get_busy():
        pass


def 입력한글자읽기():
    pygame.mixer.init()  # ⑤ 소리 도구 준비
    while True:  # ① 무한 반복 조건
        text = input("읽을 문장을 입력하세요 (종료하려면 'q' 입력): ")

        if text == "q":  # ② 종료 글자 조건
            print("종료합니다.")
            break  # ③ 반복 탈출

        tts = gTTS(text=text, lang='ko')  # ④ 읽을 내용 넣기

        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        tts.save("input.mp3")

        pygame.mixer.music.load("input.mp3")  # ⑥ 파일 준비
        pygame.mixer.music.play()  # ⑦ 재생 시작

        while pygame.mixer.music.get_busy():
            pass  # ⑧ 재생 중 대기 키워드


입력한글자읽기()
