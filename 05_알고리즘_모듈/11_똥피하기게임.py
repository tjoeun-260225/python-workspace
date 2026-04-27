'''
위 -> 아래 떨어지면 된다.
좌 우 로 이동만 하면 된다.
'''

import pygame
import random

pygame.init()
화면 = pygame.display.set_mode((800, 600))
pygame.display.set_caption("똥피하기")
시계 = pygame.time.Clock()

폰트 = pygame.font.SysFont("malgungothic", 36)
큰폰트 = pygame.font.SysFont("malgungothic", 64)

검정 = (0, 0, 0)
하늘 = (135, 206, 235)
빨강 = (255, 50, 50)

# 이미지 불러오기
플레이어이미지 = pygame.transform.scale(pygame.image.load("images/poop_dodge/player.png").convert_alpha(), (70, 70))
똥이미지 = pygame.transform.scale(pygame.image.load("images/poop_dodge/poop.png").convert_alpha(), (40, 40))

# 플레이어
플레이어_x = 400
플레이어_y = 530
플레이어_크기 = 35
속도 = 6

# 똥 설정
똥목록 = []
똥속도 = 4
타이머 = 0

점수 = 0
게임오버 = False

실행중 = True
while 실행중:

    for 이벤트 in pygame.event.get():
        if 이벤트.type == pygame.QUIT:
            실행중 = False
        if 이벤트.type == pygame.KEYDOWN:
            if 게임오버 and 이벤트.key == pygame.K_r:
                똥목록.clear()
                플레이어_x = 400
                점수, 똥속도, 게임오버 = 0,  4, False
    if not 게임오버:

        키 = pygame.key.get_pressed()
        if 키[pygame.K_LEFT]:  플레이어_x -= 속도
        if 키[pygame.K_RIGHT]: 플레이어_x += 속도
        플레이어_x = max(35, min(800 - 35, 플레이어_x))  # TODO 6: 화면 가로 크기

        타이머 += 1
        if 타이머 >= random.randint(20, 50):
            똥목록.append([random.randint(20, 780),-20]) # TODO 7: 똥 시작 y위치 (화면 위 밖)
            타이머 = 0

        for 똥 in 똥목록:
            똥[1] += 똥속도                                 # TODO 8: 똥 아래로 이동 (똥속도 변수)

        똥목록[:] = [똥 for 똥 in 똥목록 if 똥[1] < 650] # TODO 9: 화면 밖 기준값

        for 똥 in 똥목록:
            거리 = ((플레이어_x - 똥[0])**2 + (플레이어_y - 똥[1])**2) ** 0.5
            if 거리 < 플레이어_크기 + 20:               # TODO 10: 똥 크기 절반 (이미지 크기 40 → 20)
                게임오버 = True                           # TODO 11: 게임오버 처리

        점수 += 1
        if 점수 % 200 == 0: 똥속도 += 1

    # 화면 그리기
    화면.fill(하늘)                                        # TODO 13: 배경색

    for 똥 in 똥목록:
        화면.blit(똥이미지, (똥[0] - 20, 똥[1] - 20))   # 똥 그리기

    화면.blit(플레이어이미지, (플레이어_x - 35, 플레이어_y - 35))  # 플레이어 그리기

    pygame.draw.rect(화면, (100, 200, 100), (0, 565, 800, 35))     # 바닥

    화면.blit(폰트.render(f"점수: {점수}", True, 검정), (10, 10))
    화면.blit(폰트.render(f"속도: {똥속도}", True, 검정), (10, 50))

    if 게임오버:
        화면.blit(큰폰트.render("맞았다.", True, 빨강), (250, 230))  # TODO 14: 글자색
        화면.blit(폰트.render(f"최종 점수: {점수}", True, 검정), (310, 320))
        화면.blit(폰트.render("R 키로 재시작", True, 검정), (300, 365))

    pygame.display.flip()
    시계.tick(60)   # TODO 15: FPS

pygame.quit()