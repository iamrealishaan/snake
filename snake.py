import pygame
import random

# Initialize pygame
pygame.init()

# Set the size of the screen
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set the font
font = pygame.font.SysFont(None, 25)

# Set the clock
clock = pygame.time.Clock()

# Set the initial position of the snake
snake_block = 10
snake_speed = 15
x1 = width / 2
y1 = height / 2
x1_change = 0
y1_change = 0

# Set the initial position of the food
foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

# Define the snake function
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

# Define the main game function
def gameLoop():
    game_over = False
    game_close = False

    # Create an empty list to store the snake's position
    snake_List = []
    Length_of_snake = 1

    # Main game loop
    while not game_over:

        # Game over screen
        while game_close == True:
            screen.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            # Check for user input
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Check for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check for collision with the edges of the screen
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change
        screen.fill(white)

        # Draw the food
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

        # Add the snake's position to the list
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(sn
