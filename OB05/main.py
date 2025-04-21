import pygame
import time

pygame.init()
pygame.display.set_caption("Пинг-понг")

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
SPEED = 10

# Настройки шарика
R = 5
l_x_ball, l_y_ball = (xl + OFFSET + R), (yl + L_BOARD // 2 - R * 2)
r_x_ball, r_y_ball = (xr - OFFSET - R), (yr - L_BOARD // 2 + R * 2)
x_ball, y_ball = l_x_ball, l_y_ball
ball_speed_x = SPEED
ball_speed_y = SPEED

# Счет
FONT_SIZE = 50
font = pygame.font.Font(None, FONT_SIZE)
TEXT_POINTS_POSITION = ((WIDTH // 2 - FONT_SIZE // 2),(HEIGHT // 2 - FONT_SIZE // 2))

MAX_POINTS = 15
points_l, points_r = (0, 0)

# Главный игровой цикл
clock = pygame.time.Clock()
running = True
flag_start = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    #Старт/пауза на D
    if keys[pygame.K_d]:
        flag_start = True if not flag_start else False
        time.sleep(1)

    if flag_start:
        #Движение левой ракетки
        if keys[pygame.K_w] and yl > 0:
            yl -= SPEED
        if keys[pygame.K_s] and yl < HEIGHT - L_BOARD:
            yl += SPEED

        # Движение правой ракетки
        if keys[pygame.K_UP] and yr > 0 and flag_start:
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
            x_ball, y_ball = r_x_ball, r_y_ball

        if x_ball > WIDTH:
            points_l += 1
            x_ball, y_ball = l_x_ball, l_y_ball

    # Отрисовка
    screen.fill(WINDOW_COLOR)

    if MAX_POINTS > points_r and MAX_POINTS > points_l:
        pygame.draw.rect(screen, OBJECT_COLOR, (xl, yl, W_BOARD, L_BOARD ), 0)
        pygame.draw.rect(screen, OBJECT_COLOR, (xr, yr, W_BOARD, L_BOARD), 0)
        pygame.draw.circle(screen, OBJECT_COLOR, (x_ball, y_ball), R, 5)
        text_surface = font.render((str(points_l) + ":" + str(points_r)), True, OBJECT_COLOR)
        screen.blit(text_surface, TEXT_POINTS_POSITION)
    else:
        # Задаем победителя
        gamer = "левый" if points_l > points_r else "правый"
        text_game_over = f"Победил {gamer} игрок"
        text_game_over_surface = font.render(text_game_over, True, OBJECT_COLOR)

        # Получаем размеры текстовой поверхности
        text_width, text_height = text_game_over_surface.get_size()

        # Рассчитываем позицию для центрирования текста
        text_game_over_position = ((WIDTH - text_width) // 2, (HEIGHT - text_height) // 2)

        # Отрисовываем текст
        screen.blit(text_game_over_surface, text_game_over_position)

    pygame.display.flip()  # Обновляем экран

    clock.tick(FPS) # Ограничение FPS