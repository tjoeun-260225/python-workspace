import pygame
import random

pygame.init()
화면 = pygame.display.set_mode((800, 600))
pygame.display.set_caption("런닝기사")
시계 = pygame.time.Clock()

배경 = pygame.transform.scale(pygame.image.load("images/running/background.png").convert(), (800, 600))
땅이미지 = pygame.transform.scale(pygame.image.load("images/running/ground.png").convert_alpha(), (800, 120))
플레이어이미지 = pygame.transform.scale(pygame.image.load("images/running/player.png").convert_alpha(), (70, 70))
장애물이미지 = pygame.transform.scale(pygame.image.load("images/running/obstacle.png").convert_alpha(), (60, 60))

폰트 = pygame.font.SysFont("malgungothic", 36)

땅_y = 480
플레이어_y = 땅_y - 70
플레이어_x = 100  # TODO 1에서 쓸 x 좌표
속도_y = 0
속도_x = 0  # TODO 1에서 쓸 x 속도
땅위 = True
장애물목록 = []
장애물속도 = 5
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
                플레이어_x, 플레이어_y, 속도_y, 땅위 = 100, 땅_y - 70, 0, True
                장애물목록.clear()
                점수, 장애물속도, 게임오버 = 0, 5, False

    if not 게임오버:

        키 = pygame.key.get_pressed()
        if 키[pygame.K_SPACE] and 땅위:
            속도_y - 16
            땅위 = False

        if 키[pygame.K_LEFT]:  플레이어_x -= 5
        if 키[pygame.K_RIGHT]: 플레이어_x += 5
        플레이어_x = max(0, min(800 - 70, 플레이어_x))

        속도_y += 0.8
        플레이어_y += 속도_y
        if 플레이어_y >= 땅_y - 70:
            플레이어_y, 속도_y, 땅위 = 땅_y - 70, 0, True

        타이머 += 1
        if 타이머 >= random.randint(60, 120):
            장애물목록.append(pygame.Rect(820, 땅_y - 60, 60, 60))
            타이머 = 0

        for o in 장애물목록: o.x -= 장애물속도
        장애물목록 = [o for o in 장애물목록 if o.x > -80]

        # TODO 2 완성하면 플레이어_x 도 충돌에 반영됨
        플레이어_rect = pygame.Rect(플레이어_x + 10, 플레이어_y + 10, 50, 55)
        if any(플레이어_rect.colliderect(o) for o in 장애물목록):
            게임오버 = True

        점수 += 1
        if 점수 % 300 == 0: 장애물속도 += 1

    화면.blit(배경, (0, 0))
    화면.blit(땅이미지, (0, 땅_y))
    화면.blit(플레이어이미지, (int(플레이어_x), int(플레이어_y)))  # TODO 2 완성하면 플레이어_x 가 움직임
    for o in 장애물목록: 화면.blit(장애물이미지, (o.x, o.y))
    화면.blit(폰트.render(f"점수:{점수}", True, (255, 255, 255)), (10, 10))

    if 게임오버:
        화면.blit(폰트.render("게임 종료 | R 재시작", True, (255, 50, 50)), (230, 270))
        화면.blit(폰트.render(f"최종 점수 : {점수}", True, (255, 255, 0)), (300, 320))

    pygame.display.flip()
    시계.tick(60)

pygame.quit()
