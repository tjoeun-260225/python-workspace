'''
python 으로 가볍게 게임을 만드는 라이브러리

화면에 도형/이미지 그리기
키보드/마우스 실시간 감지
소리 재생
애니메이션

설치방법 pip install pygame
import pygame  # pete shinners -> C 언어를 사용하는 개발자인데 파이썬에서 게임 개발 도구가 부족하다판단해서 개발
코드 공개하고 유지보수 기여를 2006 이후로 거의 안했으나 파이썬 pygame 사용하는 커뮤니티 유저들이 개발 유지

pygame 커뮤니티 안에서 팀이 갈라짐
┌──── pygame(원조)
└──── pygame-ce(활발하게 개발 중)
'''
# import tkinter as tk -> 파이썬 개발자가 만들었음 만든사람들의 룰이 있음
import pygame

pygame.init()  # pygame. 초기세팅
화면 = pygame.display.set_mode((800, 600))  # 창 크기 # pete shinners 만들 때 800x600 보다 (800, 600) 선호했다.
pygame.display.set_caption("공 움직이기")  # 창 제목
시계 = pygame.time.Clock()  # FPS 조절용

# 공 초기 설정
공_x = 400
공_y = 300
공크기 = 20
속도 = 5
# 튜플 형태로 해서 흰색 컬러 추후 변경 불가하게 값 설정
흰색 = (255, 255, 255)  # 255 = F
검정 = (0, 0, 0)
빨강 = (255, 0, 0)

# 게임 루프 (Tkinter의 mainloop 같은 것)
실행중 = True
while 실행중:

    # 1. 이벤트 처리
    for 이벤트 in pygame.event.get():
        if 이벤트.type == pygame.QUIT:  # x버튼을 마우스로 클릭하면
            실행중 = False

    # 키보드 입력으로 공 이동
    키 = pygame.key.get_pressed()         # 키 안에 모든 키 의 상태변수가 들어있는 상태
    if 키[pygame.K_LEFT]: 공_x -= 속도    # 공x 가로 위치를 x가 줄면 왼쪽 이동
    if 키[pygame.K_RIGHT]: 공_x += 속도   # 공x 가 늘면 속도만큼 오른쪽으로 이동
    if 키[pygame.K_UP]: 공_y -= 속도      # 공y 가 줄면 위쪽으로 이동
    if 키[pygame.K_DOWN]: 공_y += 속도    # 공y 가 늘면 아래쪽 이동

    # 벽충돌(화면 밖으로 공이 나가지 못하게
    공_x = max(공크기, min(800 - 공크기, 공_x))
    공_y = max(공크기, min(600 - 공크기, 공_y))

    # 2. 화면 그리기
    # 화면.fill(검정)  # 화면 배경색 (R, G, B)  255,255,255 화이트
    pygame.draw.circle(화면, 빨강, (공_x, 공_y), 공크기)

    pygame.display.flip()  # 화면 갱신
    시계.tick(60)  # 초당 60 프레임

pygame.quit()
