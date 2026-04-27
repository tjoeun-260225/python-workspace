# 키 입력으로 공 색상 변경하기
# 현재색에서 키 입력으로 색상을 변경할 수 있다.
import pygame

pygame.init()
화면 = pygame.display.set_mode((800, 600))
pygame.display.set_caption("색 바꾸는 공")
시계 = pygame.time.Clock()

공_x = 400
공_y = 300
공크기 = 20
속도 = 5

검정 = (0, 0, 0)
현재색 = (255, 255, 255)  # 공 색을 변수로 관리 (처음엔 흰색)

실행중 = True
while 실행중:

    for 이벤트 in pygame.event.get():
        if 이벤트.type == pygame.QUIT:
            실행중 = False

    키 = pygame.key.get_pressed()

    # ── 공 이동 ──────────────────────────────
    if 키[pygame.K_LEFT]:  공_x -= 속도
    if 키[pygame.K_RIGHT]: 공_x += 속도
    if 키[pygame.K_UP]:    공_y -= 속도
    if 키[pygame.K_DOWN]:  공_y += 속도

    # ── 벽 충돌 ──────────────────────────────
    공_x = max(공크기, min(800 - 공크기, 공_x))
    공_y = max(공크기, min(600 - 공크기, 공_y))

    # ── 색 변경 ──────────────────────────────
    if 키[pygame.K_r]: 현재색 = (255, 0, 0)       # R키 → 빨강
    if 키[pygame.K_g]: 현재색 = (0, 255, 0)       # G키 → 초록
    if 키[pygame.K_b]: 현재색 = (0, 0, 255)       # B키 → 파랑
    if 키[pygame.K_SPACE]: 현재색 = (255, 255, 255)   # 스페이스 → 흰색

    # ── 화면 그리기 ───────────────────────────
    화면.fill(검정)                                 # 배경 검정으로 채우기
    pygame.draw.circle(화면,현재색, (공_x, 공_y), 공크기)  # 공 그리기

    pygame.display.flip()
    시계.tick(60)    # 초당 몇 프레임?

    pygame.quit()