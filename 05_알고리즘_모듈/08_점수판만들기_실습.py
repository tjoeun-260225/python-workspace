'''
점수 한글 깨지지 않게 설정
몇 초안에 랜덤으로 만들어진 별을 먹지 못하면 점수 - 처리 점수 + 에서 0이되면 게임 종료

'''
import pygame
import random

pygame.init()
화면 = pygame.display.set_mode((800, 600))
pygame.display.set_caption("별 먹기 게임")
시계 = pygame.time.Clock()

검정 = (0, 0, 0)
빨강 = (255, 0, 0)
노랑 = (255, 255, 0)
흰색 = (255, 255, 255)

공크기 = 20
별크기 = 10
속도 = 5

공_x = 400
공_y = 300

별_x = random.randint(별크기, 800 - 별크기)
별_y = random.randint(별크기, 600 - 별크기)

점수 = 0

# 시스템 한글 폰트 주가
폰트 = pygame.font.Font(None, 36)

실행중 = True
while 실행중:

    for 이벤트 in pygame.event.get():
        if 이벤트.type == pygame.QUIT:
            실행중 = False

    키 = pygame.key.get_pressed()
    if 키[pygame.K_LEFT]:  공_x -= 속도
    if 키[pygame.K_RIGHT]: 공_x += 속도
    if 키[pygame.K_UP]:    공_y -= 속도
    if 키[pygame.K_DOWN]:  공_y += 속도

    공_x = max(공크기, min(800 - 공크기, 공_x))
    공_y = max(공크기, min(600 - 공크기, 공_y))

    거리 = ((공_x - 별_x) ** 2 + (공_y - 별_y) ** 2) ** 0.5
    # 별 먹었을 때 처리 타이머 리셋
    if 거리 < 공크기 + 별크기:
        점수 += 1
        별_x = random.randint(별크기, 800 - 별크기)
        별_y = random.randint(별크기, 600 - 별크기)


    # 시간 초과했을 때
    # 점수 0 이 되면 게임 오버

    # 점수 0 일 때 화면 그릴 수 있고 점수 추가되었을 때 화면을 그릴 수 있다.





    화면.fill(검정)
    pygame.draw.circle(화면, 빨강, (공_x, 공_y), 공크기)
    pygame.draw.circle(화면, 노랑, (별_x, 별_y), 별크기)

    점수판 = 폰트.render(f"점수: {점수}", True, 흰색)
    화면.blit(점수판, (10, 10))

    pygame.display.flip()
    시계.tick(60)

pygame.quit()
