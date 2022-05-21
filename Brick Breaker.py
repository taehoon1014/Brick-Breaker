import pygame
import sys

pygame.init()  #pygame 초기화

#RGB 설정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# pygame 창 설정
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Brick Breaker")
clock = pygame.time.Clock()
Quit = False
clock.tick(60)

# 메인 루프
while not Quit:
    for event in pygame.event.get():  # 이벤트 처리 루프
        if event.type == pygame.QUIT:  # 종료 버튼(X)를 눌렀을 때 창 닫기
            Quit = True

        screen.fill(WHITE)
        pygame.display.flip()

# pygame, 밑 system 종료
pygame.quit()
sys.exit()