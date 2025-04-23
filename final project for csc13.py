import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display Dimensions
dis_width = 800
dis_height = 600

# Create Display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Poornima')

# Clock to control game speed
clock = pygame.time.Clock()

# Snake Block Size and Speed
snake_block = 20
snake_speed = 15

# Font Style
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

# set up player.object
player_pos = pygame.Rect(300,200,50,50) # rectangular coordinates
# (left, top, width,height)
player_speed = 5
# set up wall
wall = pygame.Rect(100,200,10, 100)

# game loop
running = True
while running:
    pygame.time.delay(30)  # slow down the loop
    dis.fill(white)
    
# event handling; in this example, quitting the game
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            running = false

# copy the original position
    old_psition = player_pos.copy()

# Key press handling; in this example, for moving player rect object
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] :
        player_po.x -= player_speed
    if keys[pygame.K_RIGHT] :
      player_pos.x += player_speed
    if keys[pygame.K_UP] :
        player_pos.y -= player_speed
    if keys[pygame.K_DOWN] :
        player_pos.y += player_speed

# Collision check: move back if we hit the wall
    if player_pos.colliderect(wall) :
        player_pos = old_position # undo movement

# Draw the player
pygame.draw.rect(screen, blue, player_pos) 
# Draw wall
pygame.draw.rect(screen, Black, wall)

#update display
pygame.display.update()

pygame.quit()
sys.exit() # for smoother exit 
