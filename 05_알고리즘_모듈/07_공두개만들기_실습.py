import pygame

pygame.init()
화면 = pygame.display.set_mode((800, 600))
pygame.display.set_caption("공 두 개 움직이기")
시계 = pygame.time.Clock()

# 색깔 정의
검정 = (0, 0, 0)
빨강 = (255, 0, 0)
파랑 = (0, 0, 255)

공크기 = 20
속도 = 5

# 공 1 초기 위치 (방향키 조작)
공1_x = 200
공1_y = 300

# TODO 1: 공 2 초기 위치 변수를 만들어보기 (WASD 조작)
# 힌트: 공1이랑 겹치지 않게 x=600, y=300 정도로 시작하면 좋다
공2_x = 600
공2_y = 300

실행중 = True
while 실행중:

    for 이벤트 in pygame.event.get():
        if 이벤트.type == pygame.QUIT:
            실행중 = False

    키 = pygame.key.get_pressed()

    # 공 1 이동 (방향키)
    if 키[pygame.K_LEFT]:  공1_x -= 속도
    if 키[pygame.K_RIGHT]: 공1_x += 속도
    if 키[pygame.K_UP]:    공1_y -= 속도
    if 키[pygame.K_DOWN]:  공1_y += 속도

    # TODO 2: 공 2 이동 코드 작성 (WASD 키)
    # 힌트: pygame.K_a / pygame.K_d / pygame.K_w / pygame.K_s
    if 키[pygame.K_a]:  공2_x -= 속도
    if 키[pygame.K_d]: 공2_x += 속도
    if 키[pygame.K_w]:    공2_y -= 속도
    if 키[pygame.K_s]:  공2_y += 속도
    # 공 1 벽 충돌
    공1_x = max(공크기, min(800 - 공크기, 공1_x))
    공1_y = max(공크기, min(600 - 공크기, 공1_y))

    # TODO 3: 공 2 벽 충돌 막기
    # 힌트: 공1 벽 충돌 코드랑 동일, 변수 이름만 바꾸면 된다.
    # 공 1 벽 충돌
    공2_x = max(공크기, min(800 - 공크기, 공2_x))
    공2_y = max(공크기, min(600 - 공크기, 공2_y))
    # 화면 그리기
    화면.fill(검정)
    pygame.draw.circle(화면, 빨강, (공1_x, 공1_y), 공크기)

    # TODO 4: 공 2를 파란색으로 화면에 그려보기
    pygame.draw.circle(화면, 파랑, (공2_x, 공2_y), 공크기)


    pygame.display.flip()
    시계.tick(60)

pygame.quit()