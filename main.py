import pygame, random
from pygame.math import Vector2

# Initialize Pygame
pygame.init()

# Create screen and essentials
cell_size = 20
cell_number = 30
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# Snake class
class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)

    def draw(self):
        for block in self.body:
            block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (183, 111, 122), block_rect)

    def move(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

# Fruit class
class Fruit:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)

# Objects
snake = Snake()
fruit = Fruit()

# Game loop
screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 150)

running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == screen_update:
            snake.move()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1, 0)
                
    fruit.draw()
    snake.draw()

    pygame.display.flip()
    screen.fill((0, 0, 0))
