import pygame
import sys
import random


# 벽돌 클래스 만들기
class Brick:
    def __init__(self, x, y):
        self.start_x = x
        self.start_y = y
        self.x = 234
        self.y = 105
        self.color = random.choice(color_list)

    def draw_rectangle(self):
        pygame.draw.rect(screen, self.color, [self.start_x, self.start_y, self.x, self.y])


# 바 클래스 만들기
class Bar:
    def __init__(self):
        self.start_x = 450
        self.start_y = 885
        self.x = 300
        self.y = 15
        self.speed = 5
        self.color = random.choice(color_list)

    def draw_bar(self):
        pygame.draw.rect(screen, self.color, [self.start_x, self.start_y, self.x, self.y])


# 공 클래스 만들기
class Ball:
    def __init__(self):
        self.pos = [600, 870]
        self.radius = 15
        self.color = random.choice(color_list)

    def draw_ball(self):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)


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
color_list = [PINK, PURPLE, GREEN, RED, BLUE, YELLOW, ORANGE, BROWN]

# pygame 창 설정
size = (1200, 900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Brick Breaker")
clock = pygame.time.Clock()
Quit = False
clock.tick(60)

# 메인 루프
bar = Bar()
left_move = False
right_move = False

while not Quit:
    for event in pygame.event.get():  # 이벤트 처리 루프
        if event.type == pygame.QUIT:  # 종료 버튼(X)를 눌렀을 때 창 닫기
            Quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bar.start_x -= 5
            if event.key == pygame.K_RIGHT:
                bar.start_x += 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_move = False
            if event.key == pygame.K_RIGHT:
                right_move = False
        bar.draw_bar()
        screen.fill(WHITE)
        pygame.display.flip()

# pygame, 밑 system 종료
pygame.quit()
sys.exit()
