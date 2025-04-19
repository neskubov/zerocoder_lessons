import pygame
import time

pygame.init()
pygame.display.set_caption("Пин-понг")

# Настройки окна
WIDTH, HEIGHT = (800, 500)  # Размер окна
WINDOW_COLOR = (0, 0, 0)  # Цвет фона (чёрный)
FPS = 60                  # Частота кадров

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Настройки ракеток
W_BOARD, L_BOARD = (10, 100)
OFFSET = 10
OBJECT_COLOR = (255, 0, 0)
xl, yl = OFFSET, (HEIGHT // 2 - L_BOARD // 2)
xr, yr = (WIDTH - W_BOARD - OFFSET), (HEIGHT // 2 - L_BOARD // 2)
SPEED = 5

# Настройки шарика
R = 5
start_x_ball, start_y_ball = (xl + OFFSET + R), (yl + L_BOARD // 2 - R * 2)
x_ball, y_ball = start_x_ball, start_y_ball
ball_speed_x = SPEED
ball_speed_y = SPEED

# Счет
FONT_SIZE = 50
TEXT_POSITION = ((WIDTH // 2 - FONT_SIZE // 2),(HEIGHT // 2 - FONT_SIZE // 2))
font = pygame.font.Font(None, FONT_SIZE)
points_l, points_r = (0, 0)
max_points = 15
text_surface = font.render("0:0", True, OBJECT_COLOR)

# Главный игровой цикл
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()

    #Движение левой ракетки
    if keys[pygame.K_w] and yl > 0:
        yl -= SPEED
    if keys[pygame.K_s] and yl < HEIGHT - L_BOARD:
        yl += SPEED

    # Движение правой ракетки
    if keys[pygame.K_UP] and yr > 0:
        yr -= SPEED
    if keys[pygame.K_DOWN]  and yr < HEIGHT - L_BOARD:
        yr += SPEED

    # Движение мяча
    x_ball += ball_speed_x
    y_ball += ball_speed_y

    # Столкновение с краями экрана
    if xr <= x_ball <= xr + W_BOARD and yr <= y_ball + R <= yr + L_BOARD:
        ball_speed_x = -SPEED

    if xl <= x_ball <= xl + W_BOARD and yl <= y_ball + R <= yl + L_BOARD:
        ball_speed_x = +SPEED

    if y_ball >= HEIGHT:
        ball_speed_y = -SPEED

    if y_ball <= 0:
        ball_speed_y = +SPEED

    if x_ball < 0:
        points_r += 1
        points = str(points_r) + ":" + str(points_l)
        text_surface = font.render(points, True, OBJECT_COLOR)
        time.sleep(2)
        x_ball, y_ball = start_x_ball, start_y_ball

    if x_ball > WIDTH:
        points_l += 1
        points = str(points_r) + ":" + str(points_l)
        text_surface = font.render(points, True, OBJECT_COLOR)
        time.sleep(2)
        x_ball, y_ball = start_x_ball, start_y_ball

    # Отрисовка
    screen.fill(WINDOW_COLOR)  # Закраска фона
    pygame.draw.rect(screen, OBJECT_COLOR, (xl, yl, W_BOARD, L_BOARD ), 0)
    pygame.draw.rect(screen, OBJECT_COLOR, (xr, yr, W_BOARD, L_BOARD), 0)
    pygame.draw.circle(screen, OBJECT_COLOR, (x_ball, y_ball), R, 5)
    screen.blit(text_surface, TEXT_POSITION)

    pygame.display.flip()  # Обновляем экран

    # Ограничение FPS
    clock.tick(FPS)
    pygame.display.flip()