import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bumper Car")

clock = pygame.time.Clock()

ball1_x = WIDTH // 4
ball1_y = HEIGHT // 2
ball1_speed_x = 5
ball1_speed_y = 5

ball2_x = WIDTH // 1.5
ball2_y = HEIGHT // 2
ball2_speed_x = -2
ball2_speed_y = -2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball1_x += ball1_speed_x
    ball1_y += ball1_speed_y

    ball2_x += ball1_speed_x
    ball2_y += ball1_speed_y

    if ball1_x - BALL_RADIUS < 0 or ball1_x + BALL_RADIUS > WIDTH:
        ball1_speed_x = -ball1_speed_x

    if ball1_y - BALL_RADIUS < 0 or ball1_y + BALL_RADIUS > HEIGHT:
        ball1_speed_y = -ball1_speed_y

    if ball2_x - BALL_RADIUS < 0 or ball2_x + BALL_RADIUS > WIDTH:
        ball2_speed_x = -ball2_speed_x

    if ball2_y - BALL_RADIUS < 0 or ball2_y + BALL_RADIUS > HEIGHT:
        ball2_speed_y = -ball2_speed_y

    screen.fill(BLACK)

    pygame.draw.circle(screen, WHITE, (int(ball1_x), int(ball1_y)), BALL_RADIUS)

    pygame.draw.circle(screen, WHITE, (int(ball2_x), int(ball2_y)), BALL_RADIUS)

    pygame.display.flip()

    clock.tick(FPS)