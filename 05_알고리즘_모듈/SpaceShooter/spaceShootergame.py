import pygame
import random

pygame.init()
화면 = pygame.display.set_mode((800, 600))
pygame.display.set_caption("우주 피하기")
시계 = pygame.time.Clock()

폰트 = pygame.font.SysFont("malgungothic", 36)
큰폰트 = pygame.font.SysFont("malgungothic", 64)

# 이미지 불러오기
배경이미지 = pygame.transform.scale(pygame.image.load("background.png").convert(), (800, 600))
플레이어이미지 = pygame.transform.scale(pygame.image.load("player.png").convert_alpha(), (60, 70))
금화이미지 = pygame.transform.scale(pygame.image.load("hp.png").convert_alpha(), (40, 40))

# 플레이어 설정
플레이어_x = 400
플레이어_y = 500
플레이어_속도 = 6

# 운석 설정
운석목록 = []
운석속도 = 4

# 금화 설정
금화목록 = []
금화속도 = 3

운석타이머 = 0
금화타이머 = 0
점수 = 50
게임오버 = False

실행중 = True
while 실행중:

    for 이벤트 in pygame.event.get():
        if 이벤트.type == pygame.QUIT:
            실행중 = False
        if 이벤트.type == pygame.KEYDOWN:
            if 게임오버 and 이벤트.key == pygame.K_r:
                # TODO 4: 재시작 초기화
                운석목록.clear()
                금화목록.clear()
                플레이어_x = 400
                점수 = 50
                게임오버 = False

    if not 게임오버:

        키 = pygame.key.get_pressed()
        if 키[pygame.K_LEFT]:  플레이어_x -= 플레이어_속도
        if 키[pygame.K_RIGHT]: 플레이어_x += 플레이어_속도
        플레이어_x = max(30, min(800 - 30, 플레이어_x))
        # 운석 생성
        운석타이머 += 1
        if 운석타이머 >= random.randint(30, 60):
            운석목록.append([random.randint(20, 780), -20])
            운석타이머 = 0

        # 금화 생성
        금화타이머 += 1
        if 금화타이머 >= random.randint(60, 120):
            금화목록.append([random.randint(20, 780), -20])
            금화타이머 = 0

        # 운석 이동
        for 운석 in 운석목록:
            운석[1] += 운석속도
        운석목록[:] = [o for o in 운석목록 if o[1] < 650]

            # 금화 이동
        for 금화 in 금화목록:
            금화[1] += 금화속도                             # TODO 11: 금화속도 변수
        금화목록[:] = [o for o in 금화목록 if o[1] < 650]

        # 운석 충돌 → 점수 -10
        for 운석 in 운석목록:
            거리 = ((플레이어_x - 운석[0])**2 + (플레이어_y - 운석[1])**2) ** 0.5
            if 거리 < 45:           # TODO 12: 충돌 거리 (힌트: 40~50)
                점수 -= 10          # 점수 -= -10  점수가 차감이 되는것이 아니라 점수 +10 가 된다.
                운석목록.remove(운석)
                break

        # 금화 충돌 → 점수 +20
        for 금화 in 금화목록:
            거리 = ((플레이어_x - 금화[0])**2 + (플레이어_y - 금화[1])**2) ** 0.5
            if 거리 < 40:
                점수 += 20
                금화목록.remove(금화)
                break

        if 점수 <= 0:
            게임오버 = True

    # 화면 그리기
    화면.blit(배경이미지, (0, 0))           # TODO 17: 배경 이미지 변수

    for 운석 in 운석목록:
        pygame.draw.circle(화면, (150, 150, 150), (운석[0], 운석[1]), 20)
        pygame.draw.circle(화면, (100, 100, 100), (운석[0]-5, 운석[1]-5), 8)

    for 금화 in 금화목록:
        화면.blit(금화이미지, (금화[0] - 20, 금화[1] - 20))

    화면.blit(플레이어이미지, (플레이어_x - 30, 플레이어_y - 35))
    화면.blit(폰트.render(f"점수: {점수}", True, (255, 255, 255)), (10, 10))

    if 게임오버:
        화면.blit(큰폰트.render("GAME OVER", True, (255, 50, 50)), (220, 240))
        화면.blit(폰트.render(f"최종 점수: {점수}", True, (255, 255, 0)), (300, 320))
        화면.blit(폰트.render("R 키로 재시작", True, (255, 255, 255)), (295, 370))

    pygame.display.flip()
    시계.tick(60)   # TODO 18: FPS

pygame.quit()