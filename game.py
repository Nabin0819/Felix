import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 300
GROUND_HEIGHT = 230
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load assets
DINO_IMG = pygame.image.load("dino.png")
CACTUS_IMG = pygame.image.load("cactus.png")

# Scale images
DINO_IMG = pygame.transform.scale(DINO_IMG, (50, 50))
CACTUS_IMG = pygame.transform.scale(CACTUS_IMG, (30, 50))

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Dino:
    def __init__(self):
        self.image = DINO_IMG
        self.x = 50
        self.y = GROUND_HEIGHT
        self.jump = False
        self.velocity = 0

    def update(self):
        if self.jump:
            self.y += self.velocity
            self.velocity += 1
            if self.y >= GROUND_HEIGHT:
                self.y = GROUND_HEIGHT
                self.jump = False
                self.velocity = 0

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class Cactus:
    def __init__(self):
        self.image = CACTUS_IMG
        self.x = WIDTH
        self.y = GROUND_HEIGHT

    def update(self):
        self.x -= 5
        if self.x < -30:
            self.x = WIDTH + random.randint(0, 200)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

def game_loop():
    dino = Dino()
    cactus = Cactus()
    running = True

    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and dino.y == GROUND_HEIGHT:
                    dino.jump = True
                    dino.velocity = -10

        dino.update()
        cactus.update()

        dino.draw()
        cactus.draw()

        pygame.display.update()
        clock.tick(30)

    pygame.quit()

game_loop()
