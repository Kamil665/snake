import pygame
import random

pygame.init()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
cell_size = 20
WIDTH = 800
HEIGHT = 600
SNAKE = [(5, 5), (4, 5), (3, 5)]
width = WIDTH // cell_size
height = HEIGHT // cell_size
dx, dy = 1, 0
score = 0
font = pygame.font.SysFont('Arial', 20)

def generate_apple():
    while True:
        pos = (random.randint(0, width - 1), random.randint(0, height - 1))
        if pos not in SNAKE:
            return pos
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    return (x, y)

def draw_snake(screen, snake):
    for x, y in snake:
        pygame.draw.rect(screen, RED, pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size))

def reset_game():
    global SNAKE, dx, dy, apple_pos, score
    SNAKE = [(5, 5), (4, 5), (3, 5)]
    dx, dy = 1, 0
    apple_pos = generate_apple()
    score = 0

screen = pygame.display.set_mode((800, 600))

apple_pos = generate_apple()
clock = pygame.time.Clock()

running = True

while running:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dx, dy = 0, -1
            elif event.key == pygame.K_DOWN:
                dx, dy = 0, 1
            elif event.key == pygame.K_LEFT:
                dx, dy = -1, 0
            elif event.key == pygame.K_RIGHT:
                dx, dy = 1, 0

    head_x, head_y = SNAKE[0]
    new_head = (((head_x + dx) % width), (head_y + dy) % height)

    if new_head in SNAKE:
        reset_game()
        continue

    if new_head == apple_pos:
        SNAKE.insert(0, new_head)
        apple_pos = generate_apple()
        score += 1
    else:
        SNAKE.insert(0, new_head)
        SNAKE.pop()

    screen.fill(BLUE)
    draw_snake(screen, SNAKE)

    pygame.draw.rect(screen, GREEN, (apple_pos[0] * cell_size, apple_pos[1] * cell_size, cell_size, cell_size))

    text = font.render(f"Счёт: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()