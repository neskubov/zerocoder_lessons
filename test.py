import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_SPEED = 5
ENEMY_SPEED = 3

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра в стиле ООП")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_UP]:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            self.rect.y += PLAYER_SPEED

        # Ограничение игрока в пределах экрана
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect(
            center=(random.randint(0, WIDTH), random.randint(0, HEIGHT))
        )
        self.speed = ENEMY_SPEED

    def update(self):
        # Движение врага вниз
        self.rect.y += self.speed
        # Если враг выходит за пределы экрана, он появляется сверху
        if self.rect.y > HEIGHT:
            self.rect.y = -self.rect.height
            self.rect.x = random.randint(0, WIDTH - self.rect.width)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(
            center=(random.randint(0, WIDTH), random.randint(0, HEIGHT))
        )

    def reset_position(self):
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))


class Game:
    def __init__(self):
        self.running = True
        self.player = Player()
        self.enemies = pygame.sprite.Group(Enemy() for _ in range(5))
        self.coins = pygame.sprite.Group(Coin() for _ in range(3))
        self.all_sprites = pygame.sprite.Group(self.player, self.enemies, self.coins)
        self.score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)
        self.enemies.update()

        # Проверка столкновений
        if pygame.sprite.spritecollideany(self.player, self.enemies):
            print("Game Over!")
            self.running = False

        coins_collected = pygame.sprite.spritecollide(self.player, self.coins, dokill=True)
        for coin in coins_collected:
            self.score += 1
            print(f"Score: {self.score}")
            coin.reset_position()
            self.coins.add(coin)

    def draw(self):
        screen.fill(BLACK)
        self.all_sprites.draw(screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()