import pygame
import time

# Инициализация Pygame
pygame.init()
pygame.display.set_caption("Пинг-понг")

# Настройки окна
WIDTH, HEIGHT = 800, 500
WINDOW_COLOR = (0, 0, 0)
FPS = 60

# Настройки ракеток
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_OFFSET = 10
PADDLE_COLOR = (255, 0, 0)
PADDLE_SPEED = 10

# Настройки шарика
BALL_RADIUS = 5
BALL_SPEED = 10

# Счет и размер шрифта
FONT_SIZE = 25
FONT_COLOR = (255, 0, 0)
MAX_POINTS = 15

# Инициализация объектов
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font("Roboto-Italic-VariableFont_wdth,wght.ttf", FONT_SIZE)
clock = pygame.time.Clock()

# Начальные позиции объектов
def reset_game():
    """Сбрасывает игру к начальному состоянию."""
    global left_paddle, right_paddle, ball, ball_speed_x, ball_speed_y, points_left, points_right, game_active
    left_paddle = pygame.Rect(PADDLE_OFFSET, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = pygame.Rect(WIDTH - PADDLE_WIDTH - PADDLE_OFFSET, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
    ball_speed_x, ball_speed_y = BALL_SPEED, BALL_SPEED
    points_left, points_right = 0, 0
    game_active = False

reset_game()

def reset_ball():
    """Сброс позиции мяча в центр."""
    ball.x, ball.y = WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS
    return BALL_SPEED if points_left <= points_right else -BALL_SPEED, BALL_SPEED

def draw_objects():
    """Рисует все игровые объекты."""
    screen.fill(WINDOW_COLOR)
    pygame.draw.rect(screen, PADDLE_COLOR, left_paddle)
    pygame.draw.rect(screen, PADDLE_COLOR, right_paddle)
    pygame.draw.ellipse(screen, PADDLE_COLOR, ball)
    text_surface = font.render(f"{points_left}:{points_right}", True, FONT_COLOR)
    screen.blit(text_surface, ((WIDTH - text_surface.get_width()) // 2, 10))

def draw_winner():
    """Отображает экран победителя."""
    winner = "левый" if points_left > points_right else "правый"
    text_surface = font.render(f"Победил {winner} игрок! (Нажмите R, чтобы перезапустить)", True, FONT_COLOR)
    screen.blit(text_surface, ((WIDTH - text_surface.get_width()) // 2, (HEIGHT - text_surface.get_height()) // 2))

# Главный игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
# Старт/пауза игры (клавиша D)
    if keys[pygame.K_d]:
        game_active = not game_active
        time.sleep(0.3)  # Задержка для предотвращения множественных переключений

    # Перезапуск игры (клавиша R)
    if keys[pygame.K_r]:
        reset_game()
        time.sleep(0.3)  # Задержка для предотвращения множественных переключений

    if game_active and points_left < MAX_POINTS and points_right < MAX_POINTS:
        # Движение левой ракетки
        if keys[pygame.K_w] and left_paddle.top > 0:
            left_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
            left_paddle.y += PADDLE_SPEED

        # Движение правой ракетки
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
            right_paddle.y += PADDLE_SPEED

        # Движение мяча
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Отражение мяча от верхнего и нижнего края
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y = -ball_speed_y

        # Отражение мяча от ракеток
        if ball.colliderect(left_paddle) and ball_speed_x < 0:
            ball_speed_x = -ball_speed_x
        if ball.colliderect(right_paddle) and ball_speed_x > 0:
            ball_speed_x = -ball_speed_x

        # Проверка на голы
        if ball.left <= 0:
            points_right += 1
            ball_speed_x, ball_speed_y = reset_ball()
        if ball.right >= WIDTH:
            points_left += 1
            ball_speed_x, ball_speed_y = reset_ball()

    # Отрисовка
    if points_left < MAX_POINTS and points_right < MAX_POINTS:
        draw_objects()
    else:
        draw_winner()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()