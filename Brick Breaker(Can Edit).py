import math
import pygame
import sys
import random


# 벽돌 클래스 만들기
class Brick:
    def __init__(self, x, y):
        self.start_x = x
        self.start_y = y
        self.x = 234  # 가로 5개
        self.y = 105  # 세로 4개
        self.color = random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)

    def draw_rectangle(self):
        pygame.draw.rect(screen, self.color, [self.start_x, self.start_y, self.x, self.y])


# 바 클래스 만들기
class Bar:
    def __init__(self):
        self.start_x = 450
        self.start_y = 870
        self.x = 300
        self.y = 25
        self.speed = 1
        self.color = random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)

    def draw_bar(self):
        pygame.draw.rect(screen, self.color, [self.start_x, self.start_y, self.x, self.y])


# 공 클래스 만들기
class Ball:
    def __init__(self):
        self.ball_img = pygame.image.load("진짜 공.png")
        self.ball_img = pygame.transform.scale(self.ball_img, (50, 50))
        self.speed = 1
        self.start_x = 575
        self.start_y = 810
        self.direction = 0
        while not ((20 <= self.direction <= 70) or (110 <= self.direction <= 160)):  # 처음 각도 조정
            self.direction = random.randint(20, 160)
        self.move_x = math.cos(math.pi * (self.direction / 180))
        self.move_y = math.sin(math.pi * (self.direction / 180))

    def draw_ball(self):
        screen.blit(self.ball_img, (self.start_x, self.start_y))


pygame.init()  # pygame 초기화

# RGB 설정
PINK = (255, 182, 193)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (139, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 127, 0)
BROWN = (163, 111, 64)
color_list = [PINK, PURPLE, GREEN, RED, BLUE, YELLOW, ORANGE, BROWN, BLACK]

# pygame 창 설정
size = (1200, 900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Brick Breaker")
clock = pygame.time.Clock()
Quit = False
clock.tick(60)

#게임 대기화면
SB = 0
while SB == 0:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                SB = 1
    screen.fill(BLACK)
    font = pygame.font.Font("C:/Users/배유찬/AppData/Local/Microsoft/Windows/Fonts/neodgm.ttf", 30)
    text = font.render("PRESS SPACE KEY TO START THE GAME", True, (255, 0, 0))
    screen.blit(text, (350, round(size[1] / 2 - 50)))
    pygame.display.flip()

# 메인 루프
GO = 0
bar = Bar()
brick_list = []
ball = Ball()
for i in range(5):
    for j in range(4):
        brick = Brick(5 + 239 * i, 5 + 110 * j)
        brick_list.append(brick)
left_move = False
right_move = False

while not Quit:
    for event in pygame.event.get():  # 이벤트 처리 루프
        if event.type == pygame.QUIT:  # 종료 버튼(X)를 눌렀을 때 창 닫기

            Quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_move = True
            if event.key == pygame.K_RIGHT:
                right_move = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_move = False
            if event.key == pygame.K_RIGHT:
                right_move = False
    if left_move:
        bar.start_x -= bar.speed
    elif right_move:
        bar.start_x += bar.speed
    if bar.start_x < 0:
        bar.start_x = 0
    elif bar.start_x > 900:
        bar.start_x = 900

    screen.fill(BLACK)
    bar.draw_bar()
    ball.draw_ball()
    ball.start_x -= ball.speed * ball.move_x
    ball.start_y -= ball.speed * ball.move_y

    # 왼쪽 벽 부딪혔을 때
    if ball.start_x <= 0:
        ball.move_x = -ball.move_x

    # 오른쪽벽 부딪혔을 때
    elif ball.start_x >= 1150:
        ball.move_x = -ball.move_x

    # 윗쪽 벽 부딪혔을 때
    elif ball.start_y <= 0:
        ball.move_y = -ball.move_y

    # 공이 땅에 떨어졌을떄
    elif ball.start_y > 900:
        GO = 1
        Quit = True

    # 바에 부딪혔을때
    if ball.start_y >= 820 and (bar.start_x <= ball.start_x <= (bar.start_x + 300)): # 윗쪽
        ball.move_y = -ball.move_y

    # 벽돌에 부딪혔을떄
    num_bricks = len(brick_list)
    num = -1
    for i in range(num_bricks):
        num = i
        this_brick_x = brick_list[i].start_x
        this_brick_y = brick_list[i].start_y
        """
        공 전체 크기: 50x50
        벽돌 전체 크기: 234x105
        벽돌 간격 포함: 239x110
        """
        if this_brick_y - 50 <= ball.start_y < this_brick_y and this_brick_x - 25 < ball.start_x < this_brick_x + 234 - 25:  # 벽돌 위
            ball.move_y = -ball.move_y
            break
        elif this_brick_y + 105 - 50 < ball.start_y <= this_brick_y + 105 and this_brick_x - 25 < ball.start_x < this_brick_x + 234 - 25:  # 벽돌 아래
            ball.move_y = -ball.move_y
            break
        elif this_brick_y - 25 < ball.start_y < this_brick_y + 105 - 25 and this_brick_x - 50 <= ball.start_x < this_brick_x - 25:  # 벽돌 왼쪽
            ball.move_x = -ball.move_x
            break
        elif this_brick_y - 25 < ball.start_y < this_brick_y + 105 - 25 and this_brick_x + 234 - 25 <= ball.start_x <= this_brick_x + 234:  # 벽돌 오른쪽
            ball.move_x = -ball.move_x
            break
        else:
            num = -1

    if num != -1:
        del brick_list[num]

    for i in range(len(brick_list)):
        brick_list[i].draw_rectangle()
    pygame.display.flip()

# pygame, 밑 system 종료
while GO == 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    font = pygame.font.Font("C:/Users/배유찬/AppData/Local/Microsoft/Windows/Fonts/neodgm.ttf", 120)
    text = font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(text, (330, round(size[1] / 2 - 80)))
    pygame.display.flip()
pygame.quit()
sys.exit()
