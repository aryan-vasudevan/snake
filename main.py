import pygame, random
from pygame.math import Vector2

# Initialize Pygame
pygame.init()

# Create screen and essentials
cell_size = 30
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
            if block == self.body[0]:
                screen.blit(snake_head_sprite, (block.x * cell_size, block.y * cell_size))
            else:
                screen.blit(snake_body_sprite, (block.x * cell_size, block.y * cell_size))

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

        while self.pos in snake.body:
            self.x = random.randint(0, cell_number - 1)
            self.y = random.randint(0, cell_number - 1)
                

    def draw(self):
        screen.blit(fruit_sprite, (self.pos.x * cell_size, self.pos.y * cell_size))

# Sprites
fruit_sprite = pygame.image.load("img/Apple/apple.png")
fruit_sprite = pygame.transform.scale(fruit_sprite, (cell_size , cell_size))

snake_head_sprite_up = pygame.image.load("img/Snake/snake_head_up.png")
snake_head_sprite_up = pygame.transform.scale(snake_head_sprite_up, (cell_size , cell_size))

snake_head_sprite_down = pygame.image.load("img/Snake/snake_head_down.png")
snake_head_sprite_down = pygame.transform.scale(snake_head_sprite_down, (cell_size , cell_size))

snake_head_sprite_left = pygame.image.load("img/Snake/snake_head_left.png")
snake_head_sprite_left = pygame.transform.scale(snake_head_sprite_left, (cell_size , cell_size))

snake_head_sprite_right = pygame.image.load("img/Snake/snake_head_right.png")
snake_head_sprite_right = pygame.transform.scale(snake_head_sprite_right, (cell_size , cell_size))

snake_body_sprite = pygame.image.load("img/Snake/body.png")
snake_body_sprite = pygame.transform.scale(snake_body_sprite, (cell_size , cell_size))

snake_head_sprite = snake_head_sprite_down

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
                snake_head_sprite = snake_head_sprite_up
            if event.key == pygame.K_DOWN and snake.direction.y != -1:
                snake.direction = Vector2(0, 1)
                snake_head_sprite = snake_head_sprite_down
            if event.key == pygame.K_LEFT and snake.direction.x != 1:
                snake.direction = Vector2(-1, 0)
                snake_head_sprite = snake_head_sprite_left
            if event.key == pygame.K_RIGHT and snake.direction.x != -1:
                snake.direction = Vector2(1, 0)
                snake_head_sprite = snake_head_sprite_right

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