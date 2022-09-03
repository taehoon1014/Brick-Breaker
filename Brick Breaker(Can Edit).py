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
        self.speed = 4
        self.color = random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)

    def draw_bar(self):
        pygame.draw.rect(screen, self.color, [self.start_x, self.start_y, self.x, self.y])


# 공 클래스 만들기
class Ball:
    def __init__(self):
        self.ball_img = pygame.image.load("진짜 공.png")
        self.ball_img = pygame.transform.scale(self.ball_img, (50, 50))
        self.speed = 6
        self.start_x = 575
        self.start_y = 810
        self.direction = 0
        while not ((20 <= self.direction <= 70) or (110 <= self.direction <= 160)):
            self.direction = random.randint(20, 160)

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

# 메인 루프
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
    ball.start_x -= ball.speed * math.cos(math.pi * (ball.direction / 180))
    ball.start_y -= ball.speed * math.sin(math.pi * (ball.direction / 180))
    for i in range(20):
        brick_list[i].draw_rectangle()
    pygame.display.flip()

# pygame, 밑 system 종료
pygame.quit()
sys.exit()
