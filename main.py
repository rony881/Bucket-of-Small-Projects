import pygame
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity Ball")

clock = pygame.time.Clock()

# Ball properties
ball_x = 400
ball_y = 100
ball_radius = 25

velocity_y = 0
gravity = 0.5
bounce = -0.8

floor = HEIGHT - ball_radius

running = True
while running:
    clock.tick(60)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gravity
    velocity_y += gravity
    ball_y += velocity_y

    # Collision with floor
    if ball_y >= floor:
        ball_y = floor
        velocity_y *= bounce

    # making a ball
    screen.fill((30, 30, 30))
    pygame.draw.circle(screen, (255, 100, 100), (int(ball_x), int(ball_y)), ball_radius)

    pygame.display.update()

pygame.quit()
sys.exit()