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
        self.body = [Vector2(cell_number/2, cell_number/2), Vector2(cell_number/2, cell_number/2 - 1), Vector2(cell_number/2, cell_number/2 - 2)]
        self.direction = Vector2(0, 1)

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
pygame.time.set_timer(screen_update, 200)

running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == screen_update:
            snake.move()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction.y != 1:
                snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and snake.direction.y != -1:
                snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT and snake.direction.x != 1:
                snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and snake.direction.x != -1:
                snake.direction = Vector2(1, 0)

    fruit.draw()
    snake.draw()

    # Check if the snake hits the wall or itself
    if snake.body[0].x == -1 or snake.body[0].x == cell_number or snake.body[0].y == -1 or snake.body[0].y == cell_number or snake.body[0] in snake.body[1:]:
        running = False

    # Check if the snake eats the fruit
    if snake.body[0].x == fruit.pos.x and snake.body[0].y == fruit.pos.y:
        fruit = Fruit()
        fruit.draw()
        snake.body.append(snake.body[-1]) 

    pygame.display.flip()
    screen.fill((0, 0, 0))